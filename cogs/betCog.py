import cogs.ext.dbExt as dataBase
from discord.ext import commands
from pymongo import MongoClient
import discord, os



class betCog(commands.Cog):
	global db
	def __init__(self, client):
		self.client = client
		self.mclient = os.environ.get('mclient')
		self.db = MongoClient(self.mclient).Aeee.game

	@commands.command(name = 'betStart')
	async def betStart(self, ctx):
		Vrole = discord.utils.get(ctx.message.guild.roles, name = "Власть")
		Prole = discord.utils.get(ctx.message.guild.roles, name = "парламентъ")
		if Vrole in ctx.message.author.roles or Prole in ctx.message.author.roles:
			betID = ctx.message.content.split(' ')[1]
			betSubj = ctx.message.content.split(' ')[2]
			betResults = ctx.message.content.split(' ')[3]

			splittedResult = betResults.split('/')
			dbInsBody = {'betid': betID, 'bets': {'default': splittedResult}}
			self.db.insert_one(dbInsBody)

			await ctx.send(f'Принимаются ставки на {betSubj}, по исходам: {betResults}, айди: {betID}.\n*для участия пропишите $bet {betID} %ставка% %исход%.*')

	@commands.command(name = 'betEnd')
	async def betEnd(self, ctx):
		Vrole = discord.utils.get(ctx.message.guild.roles, name = "Власть")
		Prole = discord.utils.get(ctx.message.guild.roles, name = "парламентъ")
		if Vrole in ctx.message.author.roles or Prole in ctx.message.author.roles:
			betID = ctx.message.content.split(' ')[1]
			betResults = ctx.message.content.split(' ')[2]

			bets = self.db.find_one({'betid': betID})['bets']
			wValue, lValue = 0, 0

			for bet in bets:
				if betResults in bets[bet] and bet != 'default':
					uI = dataBase.UI(bet)
					dataBase.addExp(uI[1], round(int(bets[bet][0])*1.5), bet)
					wValue+= int(bets[bet][0])
				elif bet != 'default':
					uID, uExp, Ulvl, uAlias = dataBase.UI(bet)
					dataBase.addExp(uExp, round(-int(bets[bet][0])*1.5), bet)
					lvl = int(uExp ** (1/4))
					if lvl < Ulvl:
						dataBase.removeLvl(uID, lvl)
					lValue+= int(bets[bet][0])

			self.db.delete_one({'betid': betID})
			await ctx.send(f'победа исхода: {betResults} id: {betID}\n*выиграно {wValue}, проиграно {lValue}*')



	@commands.command(name = 'bet')
	async def bet(self, ctx):
		betID = ctx.message.content.split(' ')[1]
		betValue = ctx.message.content.split(' ')[2]
		betResult = ctx.message.content.split(' ')[3]

		if str(ctx.message.author.id) not in self.db.find_one({'betid': betID})['bets'] and betResult.lower() in self.db.find_one({'betid': betID})['bets']['default']:
			self.db.update({'betid': betID}, {'$set': {f'bets.{ctx.message.author.id}': (betValue, betResult)}}, multi = False)
			await ctx.send(f'вы поставили {betValue} на {betResult}')
		else:
			await ctx.send(f'произошла ошибка.\nвозможно вы уже сделали ставку или некорректен исход')



def setup(client):
	client.add_cog(betCog(client))
