import discord
from cogs.utils.skip import skip
from cogs.utils.pause import pause
from cogs.utils.resume import resume
from cogs.utils.conect import conect
from cogs.utils.desconect import desconect


class botones(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx

    @discord.ui.button(emoji="▶️", style=discord.ButtonStyle.primary, row=0) 
    async def resume_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await resume(self.ctx)
        
    @discord.ui.button(emoji="⏸️", style=discord.ButtonStyle.primary, row=0)  
    async def pause_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await pause(self.ctx)

    @discord.ui.button(emoji="⏭️", style=discord.ButtonStyle.primary, row=0)  
    async def skip_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await skip(self.ctx)

    @discord.ui.button(emoji="🟢", style=discord.ButtonStyle.success, row=1) 
    async def conect_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await conect(self.ctx)

    @discord.ui.button(emoji="🔴", style=discord.ButtonStyle.danger, row=1)  
    async def deconect_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await desconect(self.ctx)