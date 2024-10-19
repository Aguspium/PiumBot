from dotenv import load_dotenv
import os

load_dotenv()

async def mute(ctx):
    member = ctx.guild.get_member(os.getenv('DB_USERID'))
    
    if member is None:
        await ctx.send("No se encontro al usuario")
        return
    
    voice_state = member.voice
    if voice_state and voice_state.channel:
        await member.edit(mute=True)  
        await ctx.send(f'{member.display_name} ha sido muteado')
    else:
        await ctx.send(f'{member.display_name} no esta en un canal de voz')