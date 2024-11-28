from dotenv import load_dotenv
import os

load_dotenv()

async def unmute(ctx):
    member = ctx.guild.get_member(os.getenv('DB_USERID'))
    voice_state = member.voice
    if voice_state and voice_state.channel:
        await member.edit(mute=False)

