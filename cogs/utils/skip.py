from cogs.estructura import play_next, queues, current_song

async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        current_song_file = current_song.get(ctx.guild.id)
        if current_song_file:
        
            ctx.voice_client.stop()  
        
        if queues[ctx.guild.id]:
            await play_next(ctx, manual_skip=True)
        else:
            await ctx.send("No hay más canciones en la cola.")
            current_song.pop(ctx.guild.id, None)
            await ctx.voice_client.disconnect()
