import os
from discord.ext import tasks, commands
from dotenv import load_dotenv
import discord
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

class MyBot(commands.Bot):
    async def setup_hook(self):
        for directory in ['./cogs']:
            for filename in os.listdir(directory):
                if filename.endswith('.py') and filename not in ('estructura.py', 'botones.py'):
                    extension = f'{directory[2:]}.{filename[:-3]}'
                    try:
                        await self.load_extension(extension)
                        print(f'Loaded {extension}')
                    except Exception as e:
                        print(f'Failed to load extension {extension}: {e}')

    @tasks.loop(minutes=5)
    async def check_voice_status(self):
        for guild in self.guilds:
            voice_client = guild.voice_client
            if voice_client and not voice_client.is_playing() and not voice_client.is_paused():
                await voice_client.disconnect()
                print(f"Bot desconectado de {guild.name} por inactividad.")

    @check_voice_status.before_loop
    async def before_check_voice_status(self):
        await self.wait_until_ready()

bot = MyBot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Conectado como {bot.user}")

if __name__ == "__main__":
    bot.run(os.getenv('DB_TOKEN')) #asd
