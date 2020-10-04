""" Import des librairies & ressources """

# Import de l'api
from quart import Quart
from bot import bot
from os import system



""" Initialisation du serveur web """

# On init l'app
app = Quart(__name__)



""" Définition des endpoints """

# Racine
@app.route('/')
async def hello():
    return 'hello'

# Pull
@app.route('/pull')
async def pull():
    # On reboot le bot
    system('git pull && sh start.sh')
    await bot.logout()
    quit()
    return 'OK'