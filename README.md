<h1 align="center"> PiumBot </h1>

![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)
![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

## Descripcion

<p align="justify">
PiumBot es un bot de Discord básico desarrollado en Python, diseñado para ofrecer funcionalidad de reproducción de música en canales de Discord.
Su objetivo principal es proporcionar una experiencia musical fluida y eficiente dentro de los servidores de Discord.
</p>

## Funcionalidades

:heavy_check_mark: `SlashCommands` PiumBot ofrece compatibilidad con comandos slash, facilitando la interacción y el control del bot de manera intuitiva.

:heavy_check_mark: `Reproductor de Musica` Permite reproducir música obtenida a través de un título o una URL proveniente de YouTube, brindando una experiencia musical fluida y accesible en tus servidores de Discord.

:heavy_check_mark: `Descarga musica Localmente` El bot está diseñado para almacenar la música en un directorio local, lo que facilita su reproducción y garantiza una mejor calidad de audio.


## Herramientas Utilizadas

Si desea clonar mi proyecto para utilizarlo personalmente debera instalar las siguientes librerias/programas

- yt_dlp: Para descargar videos y audio desde YouTube y otros sitios web.
- discord.py: Para interactuar con la API de Discord y gestionar el bot.
- dotenv: Para cargar variables de entorno desde un archivo .env.
- FFmpeg: Para procesar y convertir archivos de audio y video.
- Python 3: El lenguaje de programación utilizado para desarrollar el bot.

## Variables de Entorno en .env

Deberá crear un archivo llamado .env en el directorio raíz del proyecto y agregar las siguientes variables de entorno:

- DB_TOKEN='su_token_de_discord'
- DB_RUTA='ruta_donde_quiera_que_se_descargue_la_musica_local'

Ejemplo de ruta para DB_RUTA: C:/piumbot/music/%(title)s.%(ext)s

Esto configurará el token de Discord para autenticar el bot y la ruta de descarga local para los archivos de música.

## Dev

| [<img src="https://avatars.githubusercontent.com/u/168209491?v=4" width=115><br><sub>Aguspium</sub>](https://github.com/Aguspium)

