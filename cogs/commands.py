from discord import app_commands
from embeds.playlist import playlist_embed 
from cogs.utils.play import play
from cogs.utils.resume import resume
from cogs.utils.skip import skip
from cogs.utils.pause import pause
from cogs.utils.conect import conect
from cogs.utils.desconect import desconect

async def setup(bot):

    @bot.hybrid_command(name='play', description='Reproduce una canción')
    @app_commands.describe(url="Link de YouTube", nombre="Nombre de la canción de YouTube")
    async def play_command(ctx, url: str = None, nombre: str = None):
        if url is None and nombre is None:
            await ctx.send("Debes elegir la opcion de Url o Nombre de cancion (youtube)")
            return

        if hasattr(ctx, 'interaction') and ctx.interaction is not None:
            await ctx.interaction.response.defer()

        query = url if url else nombre
        await play(ctx, query)

    @bot.hybrid_command(name='skip', description='Pasa al siguiente tema en la cola')
    async def skip_command(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            await skip(ctx)
        else:
            await ctx.send("No hay temas en reproduccion.")

    @bot.hybrid_command(name='playlist', description='Lista de temas en la cola')
    async def playlist_command(ctx):
        await playlist_embed(ctx)

    @bot.hybrid_command(name = "pausa", aliases=["pause"], description = "pausa el tema")
    async def pause_command(ctx):
        await pause(ctx)

    @bot.hybrid_command(name="resumen", aliases=["resume"], description= "Resume el tema pausado.")
    async def resumen_command(ctx):
        await resume(ctx)

    @bot.hybrid_command(name="leave", aliases=["desconctar"], description= "Desconecta el bot del canal de voz")
    async def desconect_command(ctx):
        await desconect(ctx)

    @bot.hybrid_command(name="conectar", aliases=["join"], description= "Conecta el bot a un canal de voz")
    async def conect_command(ctx):
        await conect(ctx)