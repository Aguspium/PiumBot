async def pause(ctx):
        if ctx.voice_client is None:
            await ctx.send("No estoy conectado a un canal de voz.")
            return

        if ctx.voice_client.is_paused():
            await ctx.send("La cancion ya esta pausada")
            return
        
        if ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("cancion pausada")