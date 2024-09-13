import os
from discord.ext import tasks, commands
from dotenv import load_dotenv
import discord
import logging

load_dotenv()
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)

#Configuraciones para Limpiar la consola
logging.getLogger('discord.voice_client').setLevel(logging.CRITICAL)
logging.getLogger('discord.gateway').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger('discord.ext.commands.bot').setLevel(logging.CRITICAL)
logging.getLogger('discord.voice_client').setLevel(logging.CRITICAL)
logging.getLogger('discord.voice_state').setLevel(logging.CRITICAL)
logging.getLogger('discord.gateway').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger('discord.ext.commands.bot').setLevel(logging.CRITICAL)
logging.getLogger('discord.player').setLevel(logging.CRITICAL)
logging.getLogger('discord.client').setLevel(logging.CRITICAL)               

#Para cargar los SlashCommands
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

#Un loop para chequear que el bot se desconecte si no hay nadie en el canal de voz.
    @tasks.loop(minutes=5)
    async def check_voice_status(self):
        for guild in self.guilds:
            voice_client = guild.voice_client
            if voice_client and not voice_client.is_playing() and not voice_client.is_paused():
                await voice_client.disconnect()

    @check_voice_status.before_loop
    async def before_check_voice_status(self):
        await self.wait_until_ready()

#Prefix para comandos comunes
bot = MyBot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Conectado como {bot.user}")

if __name__ == "__main__":
    bot.run(os.getenv('DB_TOKEN')) 
