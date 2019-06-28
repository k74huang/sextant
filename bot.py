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
            link= (message.content.replace(" ", "_"))[:-2]
            embed = discord.Embed(color=0xff66aa, title = "<osu://edit/" + link + ">")
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            # embed.add_field(name=, inline=False)
            await message.delete();
            await message.channel.send(embed=embed)

client = MyClient()
client.run('Mjk5Mjk4MTU5MTkxMTMwMTEz.XRW1nw.V4VinOaGCqnWOzWovLckj2ozsPk')