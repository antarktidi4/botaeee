from discord.ext import commands
import discord
from cogs.dbCog import UI, addExp


class card(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command('card')
	async def card(self, ctx, member: discord.Member = None):
		if member is None:
			user = ctx.message.author
			c = 'Your card!'
		elif member is not None and member.bot is False:
			user = member
			c = 'User Card!'
		else:
			embed = discord.Embed(title = 'Bot Card!', description=f"exp: ∞ (to next lvl: 0)\nlvl: ∞\npolitical coordinate: правый\nalias: None", color=0xff00f6)
			embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
			await ctx.send(embed=embed)
			return

		role = discord.utils.get(ctx.message.author.guild.roles, name="левые")
		
		if role in user.roles:
			userPolit = 'левый'
		else:
			userPolit = 'правый'

		userInfo = await UI(user.id)
		
		alias = userInfo[3]
		exp = userInfo[1]
		userLvl = userInfo[2]

		lvlExpReq = (int(exp**(1/4)) + 1)**4
		nextLvlExp = (lvlExpReq - exp) + 4

		embed = discord.Embed(title = c, description=f"exp: {exp} (to next lvl: {nextLvlExp})\nlvl: {userLvl}\npolitical coordinate: {userPolit}\nalias: {alias}", color=0xff00f6)
		embed.set_author(name = user.name, icon_url = user.avatar_url)
		await ctx.send(embed=embed)

	@commands.command('addlvl')
	async def addlvl(self, ctx):
		role = discord.utils.get(ctx.author.guild.roles, name="Власть")
		if role in ctx.message.author.roles:
			userInfo = await UI(ctx.message.author.id)
			lvlExpReq = (int(userInfo[1]**(1/4)) + 1)**4
			nextLvlExp = (lvlExpReq - userInfo[1]) + 4
			await addExp(userInfo[1], nextLvlExp, ctx.message.author.id)


		
def setup(client):
	client.add_cog(card(client))
