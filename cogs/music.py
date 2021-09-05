import discord
from discord.ext import commands
from discord.ext.commands import Cog
import youtube_dl
import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup
import requests


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print('Music up!')

    @commands.command(name='join')
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Join a voice channel first -_-")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("Heylo~, use `~~play {song name}` to play any song")
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Byee")

    @commands.command()
    async def play(self, ctx, *, arg):
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {}
        vc = ctx.voice_client

        query_string = urllib.parse.urlencode({
            'search_query': arg
        })
        htm_content = urllib.request.urlopen(
            'https://www.youtube.com/results?' + query_string
        )
        search_results = re.findall(
            r"watch\?v=(\S{11})", htm_content.read().decode())
        url = "http://www.youtube.com/watch?v=" + search_results[1]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find("meta", property="og:title")
        brr = title["content"] if title else "No meta title given"

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            await ctx.send(f"Playing {brr}")
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("Stopped ⏹️")
        

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Resumed▶️")


def setup(bot):
    bot.add_cog(Music(bot))
