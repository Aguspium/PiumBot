async def conect(ctx):

    if ctx.voice_client is not None and ctx.voice_client.is_connected():
        await ctx.send("Ya estoy en un canal de voz...")
        return

    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("Conectado al canal de voz...")
    else:
        await ctx.send("No estás en un canal de voz, no puedo conectarme.")