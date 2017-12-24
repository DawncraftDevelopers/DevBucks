import discord

client = discord.Client()

token = open("token.txt",'w')
client.run(token)
