from discord.ext import commands
import discord
from cogs.dbCog import UI, addExp


class textCommands(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command('card')
	async def card(self, ctx):
		role = discord.utils.get(ctx.message.author.guild.roles, name="правые")
		
		if role in ctx.message.author.roles:
			userPolit = 'правый'
		else:
			userPolit = 'правый'

		userInfo = UI(ctx.message.author.id)
		exp = userInfo[1]
		userLvl = userInfo[2]

		lvlExpReq = (int(exp**(1/4)) + 1)**4
		nextLvlExp = (lvlExpReq - exp) + 4

		embed = discord.Embed(title = 'Your card!', description=f"exp: {exp} (to next lvl: {nextLvlExp})\nlvl: {userLvl}\npolitical coordinate: {userPolit}", color=0xff00f6)
		embed.set_author(name = ctx.message.author, icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command('addlvl')
	async def addlvl(self, ctx):
		role = discord.utils.get(ctx.author.guild.roles, name="Власть")
		if role in ctx.message.author.roles:
			userInfo = UI(ctx.message.author.id)
			lvlExpReq = (int(userInfo[1]**(1/4)) + 1)**4
			nextLvlExp = (lvlExpReq - userInfo[1]) + 4
			addExp(userInfo[1], nextLvlExp ,ctx.message.author.id)


		
def setup(client):
	client.add_cog(textCommands(client))
