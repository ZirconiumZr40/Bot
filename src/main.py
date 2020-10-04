# Import des libs
from dotenv import load_dotenv
from os import getenv
from bot import bot
from web import app

# On load l'environement
load_dotenv()

# On démarre le serveur web
bot.loop.create_task(app.run_task('0.0.0.0', 5000))

# On connecte le bot au serveur
bot.run(getenv('TOKEN'))