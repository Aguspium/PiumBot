import discord

async def cambiar_nombre(ctx, miembro: discord.Member, *, nuevo_apodo: str = None):
    try:
        await miembro.edit(nick=nuevo_apodo)
        if nuevo_apodo:
            await ctx.reply(f"¡El apodo de {miembro.mention} ha sido cambiado a **{nuevo_apodo}**!", mention_author=False)
        else:
            await ctx.reply(f"El apodo de {miembro.mention} ha sido restablecido al nombre predeterminado.", mention_author=False)
    except discord.Forbidden:
        await ctx.reply("No tengo permisos suficientes para cambiar el apodo de este usuario.", mention_author=False)
    except Exception as e:
        await ctx.reply(f"Ha ocurrido un error: {e}", mention_author=False)