# Importation de l'api de discord
import discord

# On cree la classe du client
class MPSIClient(discord.Client):
    # Quand le bot est pret
    async def on_ready(self):
        # On log la connexion
        print('Logged on as {0}!'.format(self.user))

        # On update le status
        await self.change_presence(activity=discord.Game('https://github.com/NathanFallet/MPSI.py'))

    # Quand le bot recoit un message
    async def on_message(self, message):
        # On log le message
        print('Message from {0.author}: {0.content}'.format(message))

        # On check ce que c'est
        if message.content == 'cahierdeprepa':
            # Cahier de prepa a jour
            await message.delete()
            await message.channel.send('Le cahier de prepa est à jour !')
