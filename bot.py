import discord
import os
from datetime import datetime
from dotenv import load_dotenv
import re

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

pattern = re.compile("(([0-9,:]){3,} (\([0-9,\,|]+\) )*-)")

logFile = open(datetime.now().strftime("%c").replace(
    " ", "_").replace(":", "") + ".log", 'w+')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_guild_join(self, guild):
        print("Renko was invited to " + guild.name + "!")
        logFile.write("Renko was invited to " + guild.name + "!\n")

    async def on_message(self, message):

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # otherwise..
        if(pattern.search(message.content)):

            modder = message.author

            stringToPrint = message.content
            allLinks = pattern.findall(message.content)
            for link in allLinks:

                print("message with timestamp detected: " + message.content)
                logFile.write(
                    "message with timestamp detected: " + message.content + "\n")
                print("sent by: " + modder.display_name + "(" + modder.name + "#" + modder.discriminator + ")"
                      " at: " + datetime.now().strftime("%c") + " in #" + message.channel.name)
                logFile.write("sent by: " + modder.display_name + "(" + modder.name + "#" + modder.discriminator + ")"
                              " at: " + datetime.now().strftime("%c") + " in #" + message.channel.name + "\n")

                linkToPrint = "<osu://edit/" + \
                    link[0].replace(" ", "_")[:-2] + "> -"
                stringToPrint = stringToPrint.replace(link[0], linkToPrint)

            embed = discord.Embed(color=0xff66aa, title="",
                                  description=stringToPrint)
            embed.set_author(name=modder.display_name,
                             icon_url=message.author.avatar_url)
            await message.delete()
            await message.channel.send(embed=embed)

client = MyClient()
client.run(BOT_TOKEN)
