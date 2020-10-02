# Importation de l'api discord
from client import MPSIClient
from dotenv import load_dotenv
from os import getenv

# On load l'environement
load_dotenv()

# On demarre le bot
client = MPSIClient()
client.run(getenv('TOKEN'))