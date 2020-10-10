# Supprime tout les messages en relations avec le bots (commandes et résultats)
async def clearChannel(ctx):
    # On prend les 30 derniers messages
    messages = await ctx.message.channel.history(limit=30).flatten()
    for i in messages:
        try:
            # On checke les deux cas de figure et supprime
            if i.author.id == ctx.bot.id:
                await i.delete(delay = 0.0)
            if i.content[0] == ".":
                await i.delete(delay = 0.0)
        except:
            pass
