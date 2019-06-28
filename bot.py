import discord
import re

pattern = re.compile("([0-9,:])+ \([0-9,\,]+\) -")

currMap = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if pattern.match(message.content):
            await message.channel.send('That\'s a match! {0.author.mention}'.format(message))

client = MyClient()
client.run('Mjk5Mjk4MTU5MTkxMTMwMTEz.XRW1nw.V4VinOaGCqnWOzWovLckj2ozsPk')