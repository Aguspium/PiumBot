import discord

class ListaCancionesView(discord.ui.View):
    def __init__(self, ctx, canciones):
        super().__init__(timeout=None)
        self.ctx = ctx
        self.canciones = canciones
        self.index = 0
        self.page_size = 10  

 
    async def send_embed(self):
        embed = discord.Embed(
            title="Lista de Canciones",
            description="\n".join(self.canciones[self.index:self.index+self.page_size]),
            color=discord.Color.blue()
        )

        if len(self.canciones) > self.page_size:
            embed.set_footer(text=f"Pagina {self.index // self.page_size + 1} de {len(self.canciones) // self.page_size + 1}")
        
        await self.ctx.send(embed=embed, view=self)

    @discord.ui.button(label="Siguiente", style=discord.ButtonStyle.primary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.index + self.page_size < len(self.canciones):
            self.index += self.page_size
            await interaction.response.edit_message(embed=self.get_embed())
        else:
            await interaction.response.send_message("Ya estas en la última pagina.", ephemeral=True)

    @discord.ui.button(label="Anterior", style=discord.ButtonStyle.primary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.index - self.page_size >= 0:
            self.index -= self.page_size
            await interaction.response.edit_message(embed=self.get_embed())
        else:
            await interaction.response.send_message("Ya estas en la primera pagina.", ephemeral=True)

    @discord.ui.button(label="Buscar", style=discord.ButtonStyle.secondary)
    async def search_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = BuscarCancionModal(self.canciones)
        await interaction.response.send_modal(modal)

    def get_embed(self):
        embed = discord.Embed(
            title="Lista de Canciones",
            description="\n".join(self.canciones[self.index:self.index+self.page_size]),
            color=discord.Color.blue()
        )

        if len(self.canciones) > self.page_size:
            embed.set_footer(text=f"Pagina {self.index // self.page_size + 1} de {len(self.canciones) // self.page_size + 1}")
        
        return embed

class BuscarCancionModal(discord.ui.Modal, title="Buscar Cancion"):
    song_input = discord.ui.TextInput(label="Nombre de la cancion", placeholder="Escribe el nombre de la cancion")

    def __init__(self, canciones):
        super().__init__()
        self.canciones = canciones

    async def on_submit(self, interaction: discord.Interaction):
        song_name = self.song_input.value.lower()
        found_songs = [cancion for cancion in self.canciones if song_name in cancion.lower()]

        if found_songs:
            embed = discord.Embed(
                title="Resultados de la busqueda",
                description="\n".join(found_songs),
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="Resultados de la busqueda",
                description="No se encontraron coincidencias.",
                color=discord.Color.red()
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)