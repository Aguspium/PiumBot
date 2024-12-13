from cogs.estructura import descargar_cancion, queues, play_next

async def play(ctx, query):
        if ctx.author.voice is None:
            await ctx.send("No estas en un canal de voz")
            return

        if ctx.voice_client is None:
            try:
                await ctx.author.voice.channel.connect(timeout=30)  
            except Exception as e:
                await ctx.send(f"Error al conectar al canal de voz: {str(e)}")
                return

        try:
            file_path, title = await descargar_cancion(query)
            queues[ctx.guild.id].append({'file': file_path, 'title': title})
            await ctx.send(f"{title} **añadido a la playlist.**")

            if not ctx.voice_client.is_playing():
                await play_next(ctx)

        except Exception as e:
            await ctx.send("**No se puede agregar canciones de más de 10 minutos ni playlist.**")