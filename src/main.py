""" Import des librairies & ressources """

# Import des libs system
from dotenv import load_dotenv
from os import getenv

# Importation de l'API Discord
from discord.ext import commands
from discord import Embed, Game

# On importe nos ressources
from quotes import random_quote
from channels import channelsForResponses



""" Initialisation du bot """

# On load l'environement
load_dotenv()

# On init le bot
bot = commands.Bot(command_prefix='.')

# Quand le bot est pret
async def on_ready():
    # On log la connexion
    print('Logged on as {0}!'.format(bot.user))

    # On update le status
    await bot.change_presence(activity=Game('https://github.com/NathanFallet/MPSI.py'))



""" Définition des commandes """

# Commande de ping
async def ping(ctx):
    # On répond pong
    await ctx.channel.send('Pong')

# Guide de la contribution
async def contribution(ctx):
    # On explique comment fonctionne la contribution
    await ctx.channel.send("Pour contribuer au fonctionnement du bot et l'améliorer, rendez vous sur https://github.com/NathanFallet/MPSI.py")

# Commande de citation
async def citation(ctx):
    # On choisi une citation
    quote = random_quote()

    # On créé un embed
    embed = Embed(title=quote.text)
    embed.set_footer(text=quote.author)

    # On envoit
    await ctx.channel.send(embed=embed)



""" Définition des réponses aux messages """

# S'execute à chaque messages envoyé
@bot.event
async def on_message(message):
    # Ne répond pas à ses messages
    if message.author == bot.user:
        return

    # Gestions des commandes
    if message.content[0] == ".":
        if message.content == ".ping":
            await ping(message)
        elif message.content == ".contribution":
            await contribution(message)
        elif message.content == ".citation":
            await citation(message)

    # Ne répond pas autre part que dans #bots
    if message.channel.id not in channelsForResponses:
        return

    # Transformation en DadBot
    if "je suis " in message.content.lower():
        response = message.content.lower().split("je suis ")[1]
        await message.channel.send("Salut, " + response + ", je suis un robot !")



""" Lancement du bot """

# Ajout des listeners
bot.add_listener(on_ready)

# On le connecte au serveur
bot.run(getenv('TOKEN'))