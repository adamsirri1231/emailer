import discord
import emailer as emailer
from discord.ext import commands

client = commands.Bot(command_prefix = ",")
@client.event
async def on_ready():
    print("le bot est pret")

@client.command()
async def email(ctx,*,name):
    data = name.split(sep = " ")
    print(data)
    num = emailer.getcommandline()

    try:
        emailer.sendmail(data[0],data[1], num)
        await ctx.send(f'email had been sent to {data[0]}')
    except:
        await ctx.send(f"try typing in the following format : ,email (FullName) (Email)")

@client.command()
async def showcommands(ctx):
    file = open("commands.txt" , "r")
    data1= file.read()
    await ctx.send(data1)


client.run("OTYzMTY1NTI0MjYxNDg2NjUz.YlSHyw.oh64XYI5vepSx7W2Y0aBkmIdj9M")