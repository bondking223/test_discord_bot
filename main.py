import discord
from discord.ext import commands
from discord_components import *

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('bot ready')

@bot.command()
async def test(ctx):
    await ctx.send(
        embed=discord.Embed(title='test button'),
        components=[
            Button(style=ButtonStyle.URL,label='Youtube' ,url='https://www.youtube.com/watch?v=Bg5y1a0-Vnc'),
            Button(style=ButtonStyle.URL,label='Telegram' ,url='https://web.telegram.org/#/im')
        ]

    )
    

    resp= await bot.wait_for('button_click')
    if resp.channel == ctx.channel:
        if resp.component.lebel == "Youtube":
            await resp.respond(content='Youtube')
    

    if resp.channel == ctx.channel:
        if resp.comaponent.lebel == 'Telegram':
            await resp.respond(content='Telegram')


bot.run('ODQ5MTY0MjY5ODQ5MTQ5NDUw.YLXL2g.DqNDcWqorEBsV6yFi6KKPcAHx4E')