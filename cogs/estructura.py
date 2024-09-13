import discord
import asyncio
import yt_dlp
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
queues = defaultdict(list)
current_song = {}

async def descargar_cancion(query):
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
        'buffer_size': '64k',
        'concurrent_fragment_downloads': 1,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            'preferredquality': '160',
        }],
        'geo_bypass': True,
        'match_filter': 'vcodec: none',
        'outtmpl': os.getenv('DB_RUTA'), # Cambiar ruta de acceso a donde quieras que se descoargue la musica localmente!
        'match_filter': yt_dlp.utils.match_filter_func('duration <= 666'),
    }

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
        
    print(f"Archivo descargado en: {mp3_path}")
    return mp3_path, title

async def play_next(ctx, manual_skip=False):
    if ctx.voice_client:
        if queues[ctx.guild.id]:
            next_song = queues[ctx.guild.id].pop(0)
            
            def on_song_end(error):
                if error:
                    print(f"Error en la reproduccion: {error}")
                elif queues[ctx.guild.id]: 
                    asyncio.run_coroutine_threadsafe(play_next(ctx), ctx.bot.loop)

            source = discord.FFmpegPCMAudio(next_song['file'])
            ctx.voice_client.play(source, after=on_song_end)
            current_song[ctx.guild.id] = next_song

            if manual_skip:
                await ctx.send(f"Skipeada, ahora reproduciendo: {next_song['title']}")
        else:
            await ctx.send("No hay mas canciones en la cola.")
            current_song.pop(ctx.guild.id, None)
            await ctx.voice_client.disconnect()
    else:
        await ctx.send("No estoy conectado a un canal de voz.")
