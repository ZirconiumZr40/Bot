async def clearChannel(ctx):
    messages = await ctx.message.channel.history(limit=100).flatten()
    for i in messages:
        try:
            if i.content[0] == ".":
                await i.delete()
        except:
            pass