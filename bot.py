import discord
import re

pattern = re.compile("(([0-9,:]){3,} \([0-9,\,]+\) -)")

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
        else:
            stringToPrint = message.content;
            allLinks = pattern.findall(message.content);
            for link in allLinks:
                print(link[0])
                linkToPrint = "<osu://edit/" + link[0].replace(" ", "_")[:-2] + ">"
                stringToPrint = stringToPrint.replace(link[0], linkToPrint)
            embed = discord.Embed(color=0xff66aa, title = stringToPrint)
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
            await message.delete();
            await message.channel.send(embed=embed)

client = MyClient()
client.run('Mjk5Mjk4MTU5MTkxMTMwMTEz.XRbd1w.8nl3aQMxTwH473n4th94vSWizHw')