from cogs.estructura import current_song, descargar_cancion, queues


async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        current_song_file = current_song.get(ctx.guild.id)
        song_title = current_song_file.get('title')

        if current_song_file:
            await ctx.send(f"Cancion {song_title} Skipeada")
            ctx.voice_client.stop()  
        
        elif queues[ctx.guild.id] is False:
            
            await ctx.send("No hay más canciones en la cola.")
            current_song.pop(ctx.guild.id, None)
            await ctx.voice_client.disconnect()

