import PIL
from PIL import ImageOps, ImageFilter
import discord
from discord.ext import commands
from PIL import Image
from discord.ext.commands import Cog
import urllib
from io import BytesIO


class Imej(commands.Cog):
    def __init__(self, client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Images Up!")


    @commands.command()
    async def invert(self, ctx, usah: discord.User=None):
        if not usah:
            usah = ctx.author

        avatar_bytes = await usah.avatar_url.read()
        print(type(usah.avatar_url))
        print(usah.avatar_url)
        img = Image.open(BytesIO(avatar_bytes))
        #img = Image.open('data/ava.jpg').convert('RGB')

        if (img.mode == 'RGBA'):
            img.load()
            r, g, b, a = img.split()
            img = Image.merge('RGB', (r, g, b))
        
        img = img.filter(ImageFilter.DETAIL)
        img = img.filter(ImageFilter.SHARPEN)
        img = ImageOps.invert(img)
        img.save("data/ava.jpg")

        file = discord.File("data/ava.jpg")
        await ctx.send(file=file)

    
    @commands.command()
    async def yeet(self, ctx, usah: discord.User=None):
        if not usah:
            usah = ctx.author

        avatar_bytes = await usah.avatar_url.read()
        img = Image.open(BytesIO(avatar_bytes))
        img = img.resize((215, 215))
        yeetus = urllib.request.urlretrieve("https://i.kym-cdn.com/photos/images/newsfeed/001/610/396/66e.jpg", "data/yeet.jpg")
        deleet = Image.open("data/yeet.jpg")

        deleet.paste(img, (72, 50))
        deleet.save("data/yeet.jpg")

        file = discord.File("data/yeet.jpg")
        await ctx.send(file=file)



def setup(bot):
    bot.add_cog(Imej(bot))
