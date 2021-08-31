import discord
from discord.ext import commands
from discord.ext.commands import Cog
import youtube_dl

class Music(commands.Cog):
    def __init__(self,client):
        self.client = client


    @Cog.listener()
    async def on_ready(self):
        print('Music up!')


    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Join a voice channel first -_-")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("Heylo~, use `~~play {url}` to play any song")
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)


    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Byee")


    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)


    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")


    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed ▶️")


    @commands.command()
    async def radio(self, ctx):
        vc = ctx.author.voice.channel
        await vc.connect()
        brr = ctx.voice_client
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {}
        url = "https://www.youtube.com/watch?v=36YnV9STBqc"

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            brr.play(source)


def setup(bot):
    bot.add_cog(Music(bot))
