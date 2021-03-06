""" Import des librairies & ressources """

# Import des APIs system
from os import system

# Importation de l'API Discord
from discord.ext import commands
from discord import Embed, Game

# On importe nos ressources
from quotes import random_quote
from item_chest import generateItem
from clear import clearChannel

# Import du random
from random import randint



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
    await ctx.message.delete()



# Commande de reboot
@bot.command()
@commands.is_owner()
async def reboot(ctx):
    # On reboot le bot
    system('sh start.sh')
    await ctx.bot.logout()
    await ctx.message.delete()
    quit()



# Commande de stop
@bot.command()
@commands.is_owner()
async def stop(ctx):
    # On stop le bot
    await ctx.bot.logout()
    await ctx.message.delete()
    quit()



# Commande de clear
@bot.command()
@commands.is_owner()
async def clear(ctx):
    # On supprime tout les messages de commande et du bot du channel
    await clearChannel(ctx)
    await ctx.message.delete()



# Guide de la contribution
@bot.command()
async def contribution(ctx):
    # On explique comment fonctionne la contribution
    await ctx.send("Pour contribuer au fonctionnement du bot et l'améliorer, rendez vous sur https://github.com/MPSI1Thuillier/Bot")
    await ctx.message.delete()



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
    await ctx.message.delete()



# Commande d'item
@bot.command()
async def item(ctx):
    # On gènere un item et l'envoi
    text = generateItem()
    embed = Embed(title=text[0])
    embed.set_footer(text=text[1])

    await ctx.send(embed=embed)
    await ctx.message.delete()



# Commande de pile ou face
@bot.command()
async def pileface(ctx):
    # On décide et envoie le résultat
    await ctx.send("Le résulat est : {}".format(["Pile", "Face"][randint(0, 1)]))
    await ctx.message.delete()



# Commande de token
@bot.command()
async def token(ctx):
    # On envoi le token
    await ctx.send("Le token est : Tm9uLCBsZSB0b2tlbiBuJ2VzdCBwYXMgYWNjZXNzaWJsZSBjb21tZSDDp2E")
    await ctx.message.delete()