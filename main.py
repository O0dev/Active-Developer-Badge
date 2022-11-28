from discord.ext import commands

client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Ready!")


@client.slash_command(name="help")
async def rules(ctx):
    await ctx.respond("How can I help you?")


client.run(input("token: "))
