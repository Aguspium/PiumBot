import discord
import asyncio
import yt_dlp
import os
from dotenv import load_dotenv
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
queues = defaultdict(list)
current_song = {}
executor = ThreadPoolExecutor(max_workers=2)

async def descargar_cancion(query):
    ydl_opts = {
        'ignore-errors': True,
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
        'buffer_size': '64k',
        'signature': False,
        'concurrent_fragment_downloads': 1,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            'preferredquality': '160',
        }],
        'geo_bypass': True,
        'match_filter': 'vcodec: none',
        'outtmpl': os.getenv('DB_RUTA') + '/%(title)s.%(ext)s',
        'match_filter': yt_dlp.utils.match_filter_func('duration <= 15600'),
    }

    def descargar():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)

            file_name = ydl.prepare_filename(info['entries'][0])
            mp3_path = os.path.splitext(file_name)[0] + ".opus"
            
            if os.path.exists(mp3_path):
                title = info['entries'][0]['title']
                print(f"Cancion ya descargada: {mp3_path}")
                return mp3_path, title

            ydl.download([info['entries'][0]['webpage_url']])
            title = info['entries'][0]['title']
            return mp3_path, title

    loop = asyncio.get_event_loop()
    mp3_path, title = await loop.run_in_executor(executor, descargar)

    print(f"Archivo descargado en: {mp3_path}")
    return mp3_path, title

async def play_next(ctx):
    if ctx.voice_client:
        if queues[ctx.guild.id]:
            next_song = queues[ctx.guild.id].pop(0)

            def on_song_end(error):
                if queues[ctx.guild.id]: 
                    asyncio.run_coroutine_threadsafe(play_next(ctx), ctx.bot.loop)

            source = discord.FFmpegPCMAudio(next_song['file'])
            ctx.voice_client.play(source, after=on_song_end)
            current_song[ctx.guild.id] = next_song
            from embeds.playlist import playlist_embed
            await playlist_embed(ctx)
        else:
            await ctx.send("La cola está vacía.")
    else:
        await ctx.send("No estoy conectado a un canal de voz.")

async def obtener_canciones_descargadas():
    ruta_musica = os.getenv('DB_RUTA') 
    canciones = [f for f in os.listdir(ruta_musica) if f.endswith('.opus')]
    canciones_nombres = [os.path.splitext(cancion)[0] for cancion in canciones]
    return canciones_nombres

        