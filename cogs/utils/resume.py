async def resume(ctx):
        if ctx.voice_client is None:
            await ctx.send("No estoy conectado a un canal de voz")
            return

        if not ctx.voice_client.is_playing():
            ctx.voice_client.resume()
            await ctx.send("cancion resumida")

        else:
            await ctx.send("No hay ninguna cancion pausada")