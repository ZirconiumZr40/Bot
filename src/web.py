""" Import des librairies & ressources """

# Import de l'api
from quart import Quart



""" Initialisation du serveur web """

# On init l'app
app = Quart(__name__)



""" Définition des endpoints """

# Racine
@app.route('/')
async def hello():
    return 'hello'