async def desconect(ctx):

    if ctx.voice_client is not None and ctx.voice_client.is_connected():
        await ctx.send("Desconectando..")
        await ctx.voice_client.disconnect()

    else:
        await ctx.send("Ya estoy desconectado...")
        return

              