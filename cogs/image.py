import PIL
from PIL import ImageOps, ImageFilter
import discord
from discord.ext import commands
from PIL import Image
from discord.ext.commands import Cog
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
        yeetus = await "https://i.kym-cdn.com/entries/icons/mobile/000/031/544/cover13.jpg".read()
        deleet = Image.open(BytesIO(yeetus))

        deleet.paste(img)
        deleet.save("data/yeet.jpg")

        file = discord.File("data/yeet.jpg")
        await ctx.send(file=file)



def setup(bot):
    bot.add_cog(Imej(bot))
