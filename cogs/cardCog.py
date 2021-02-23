import cogs.ext.dbExt as dataBase
from discord.ext import commands
import discord


class card(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command('card')
	async def card(self, ctx, member: discord.Member = None):
		if member.bot is True:
			embed = discord.Embed(title = 'Bot Card!', description=f"exp: ∞ (to next lvl: 0)\nlvl: ∞\npolitical coordinate: правый\nalias: None", color=0xff00f6)
			embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
			await ctx.send(embed=embed)
			return
		user = ctx.message.author if member is None else member

		role = discord.utils.get(ctx.message.author.guild.roles, name="левые")
		userPolit = 'левый' if role in user.roles else 'правый'

		userInfo = dataBase.UI(user)
		alias = userInfo[3]
		exp = userInfo[1]
		userLvl = userInfo[2]
		lvlExpReq = (int(exp**(1/4)) + 1)**4
		nextLvlExp = (lvlExpReq - exp) + 4

		embed = discord.Embed(title = 'User Card!', description=f"exp: {exp} (to next lvl: {nextLvlExp})\nlvl: {userLvl}\npolitical coordinate: {userPolit}\nalias: {alias}", color=0xff00f6)
		embed.set_author(name = user.name, icon_url = user.avatar_url)
		await ctx.send(embed=embed)

	@commands.command('addlvl')
	async def addlvl(self, ctx):
		role = discord.utils.get(ctx.author.guild.roles, name="Власть")
		if role in ctx.message.author.roles:
			userInfo = dataBase.db.UI(ctx.message.author)
			lvlExpReq = (int(userInfo[1]**(1/4)) + 1)**4
			nextLvlExp = (lvlExpReq - userInfo[1]) + 4
			dataBase.addExp(userInfo[1], nextLvlExp, ctx.message.author.id)


def setup(client):
	client.add_cog(card(client))
