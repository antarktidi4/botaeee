from discord.ext import commands
from random import randint
import discord

reactMess = None
state = False
move = 2

class TicTacToe(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command('ttt')
	async def ttt(self, ctx, member: discord.Member):
		global reactMess, state
		state = False
		decEmoji = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣"]
		vstitle = f'tic tac toe | {ctx.message.author.mention} vs {member.mention}'
		await ctx.send(vstitle)

		dec = createDec(decEmoji)
		decMessage = await ctx.send(dec)
		reactMess = decMessage

		for e in decEmoji:
			await decMessage.add_reaction(e)


	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
		global reactMess, state
		try:
			if payload.member.bot is False and payload.message_id == reactMess.id:
				dec = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣"] if state is False else buffer('get')
				newDec = decChange(emojiMap(payload.emoji.name), dec)
				buffer(newDec)
				won = wonCheck(newDec)
				if won is None:
					await reactMess.edit(content=createDec(newDec))
				else:
					await reactMess.edit(content=createDec(newDec))
					await self.client.get_channel(payload.channel_id).send(content=won)
					state = False
					reactMess = None
		except:
			pass

	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload: discord.RawReactionActionEvent):
		if payload.message_id == reactMess.id:
			global state
			state = True




def emojiMap(emoji):
	dict = {'1⃣': 0,
			'2⃣': 1,
			'3⃣': 2,
			'4⃣': 3,
			'5⃣': 4,
			'6⃣': 5,
			'7⃣': 6,
			'8⃣': 7,
			'9⃣': 8}
	return dict[emoji]


def createDec(decEmoji):
	messBody, x = '', 0
	for c in decEmoji:
		if (x+1) % 3 == 0:
			messBody += f'{decEmoji[x]}\n'
		else:
			messBody += f'{decEmoji[x]}'
		x+=1
	return messBody


def decChange(num, dec):
	global move
	if dec[num] != ':regional_indicator_o:' and dec[num] != ':regional_indicator_x:':
		if move == 0:
			playerSymbol = ':regional_indicator_o:'
			move+=1
		elif move == 1:
			playerSymbol = ':regional_indicator_x:'
			move-=1
		else:
			if randint(0, 1) == 1:
				playerSymbol = ':regional_indicator_x:'
				move = 0
			else:
				playerSymbol = ':regional_indicator_o:'
				move = 1
		dec[num] = playerSymbol
		return dec
	else:
		return dec

buffDec = None
def buffer(dec):
	global buffDec
	if dec != 'get':
		buffDec = dec
	else:
		return buffDec

def wonCheck(dec):
	if dec[0] == ':regional_indicator_x:' and dec[1] == ':regional_indicator_x:' and dec[2] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[0] == ':regional_indicator_o:' and dec[1] == ':regional_indicator_o:' and dec[2] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[3] == ':regional_indicator_x:' and dec[4] == ':regional_indicator_x:' and dec[5] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[3] == ':regional_indicator_o:' and dec[4] == ':regional_indicator_o:' and dec[5] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[6] == ':regional_indicator_x:' and dec[7] == ':regional_indicator_x:' and dec[8] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[6] == ':regional_indicator_o:' and dec[7] == ':regional_indicator_o:' and dec[8] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[0] == ':regional_indicator_x:' and dec[3] == ':regional_indicator_x:' and dec[6] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[0] == ':regional_indicator_o:' and dec[3] == ':regional_indicator_o:' and dec[6] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[1] == ':regional_indicator_x:' and dec[4] == ':regional_indicator_x:' and dec[7] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[1] == ':regional_indicator_o:' and dec[4] == ':regional_indicator_o:' and dec[7] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[2] == ':regional_indicator_x:' and dec[5] == ':regional_indicator_x:' and dec[8] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[2] == ':regional_indicator_o:' and dec[5] == ':regional_indicator_o:' and dec[8] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[0] == ':regional_indicator_x:' and dec[4] == ':regional_indicator_x:' and dec[8] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[0] == ':regional_indicator_o:' and dec[4] == ':regional_indicator_o:' and dec[8] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	if dec[2] == ':regional_indicator_x:' and dec[4] == ':regional_indicator_x:' and dec[6] == ':regional_indicator_x:':
		return ':regional_indicator_x: win'
	elif dec[2] == ':regional_indicator_o:' and dec[4] == ':regional_indicator_o:' and dec[6] == ':regional_indicator_o:':
		return ':regional_indicator_o: win'
	else:
		return None

def setup(client):
	client.add_cog(TicTacToe(client))
