""" Import des librairies & ressources """

# Import des api system
from os import system

# Importation de l'api Discord
from discord.ext import commands
from discord import Embed, Game

# On importe nos ressources
from quotes import random_quote



""" Initialisation du bot """

# On init le bot
bot = commands.Bot(command_prefix='.')

# Quand le bot est pret
@bot.listen()
async def on_ready():
    # On log la connexion
    print('Logged on as {0}!'.format(bot.user))

    # On update le status
    await bot.change_presence(activity=Game('https://github.com/MPSI1Thuillier/Bot'))


""" Définition des commandes """

# Commande de ping
@bot.command()
async def ping(ctx):
    # On répond pong
    await ctx.send('Pong')

# Commande de reboot
@bot.command()
@commands.is_owner()
async def reboot(ctx):
    # On reboot le bot
    system('sh start.sh')
    await ctx.bot.logout()
    quit()

# Commande de stop
@bot.command()
@commands.is_owner()
async def stop(ctx):
    # On stop le bot
    await ctx.bot.logout()
    quit()

# Guide de la contribution
@bot.command()
async def contribution(ctx):
    # On explique comment fonctionne la contribution
    await ctx.send("Pour contribuer au fonctionnement du bot et l'améliorer, rendez vous sur https://github.com/MPSI1Thuillier/Bot")

# Commande de citation
@bot.command()
async def citation(ctx):
    # On choisi une citation
    quote = random_quote()

    # On créé un embed
    embed = Embed(title=quote.text)
    embed.set_footer(text=quote.author)

    # On envoit
    await ctx.send(embed=embed)