from discord.ext import commands
import discord, psycopg2, os

dbname = 'd9ehvkm8fc5u3e'
user = 'qjlbkzwsprhfjf'
password = '947b16268fb6b5bb95dc52be131a328f47ca95908364f0cef8e8a7b4273296f9'
host = 'ec2-52-21-0-111.compute-1.amazonaws.com'



db = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = db.cursor()


class UserLvl(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			if member.guild.id == 778169282655551498:
				guild = self.client.get_guild(member.guild.id)
				await member.add_roles(discord.utils.get(guild.roles, name="Рабочий класс"))
				await updateData(member)
		except AttributeError:
			pass


	@commands.Cog.listener()
	async def on_message(self, message):
		try:
			if message.author.bot is False and message.guild.id == 778169282655551498:
				if message.guild.id == 778169282655551498:
					await updateData(message.author)

					cursor.execute(f"SELECT userExp FROM users WHERE userID = '{message.author.id}'")
					for userInfo in cursor.fetchall():
						uExp = userInfo[0]
					cursor.execute(f"UPDATE users SET userExp = {uExp + 5} WHERE userID = '{message.author.id}'")
					db.commit()

					await updateLvl(message.author, message.channel)
		except AttributeError:
			pass



async def updateData(user):
	u = []
	cursor.execute(f"SELECT * FROM users")
	for dbUsers in cursor.fetchall():
		u.append(dbUsers[0])
	try:
		if str(user.id) not in u:
			cursor.execute(f"INSERT INTO users VALUES ('{user.id}', {0}, {1}, NULL)")
			db.commit()
	except:
		if str(user) not in u:
			cursor.execute(f"INSERT INTO users VALUES ('{user}', {0}, {1}, NULL)")
			db.commit()


async def updateLvl(user, channel):
	u = []
	cursor.execute(f"SELECT * FROM users WHERE userID = '{user.id}'")
	for userInfo in cursor.fetchall():
		u.append(userInfo)
	exp = userInfo[1]
	lvlStart = userInfo[2]
	lvlEnd = int(exp ** (1/4))
	if lvlStart < lvlEnd:
		await channel.send(f'{user.mention} up lvl {lvlEnd}')
		cursor.execute(f"UPDATE users SET userLvl = {lvlEnd} WHERE userID = '{user.id}'")
		db.commit()

		
		
def UI(id):
	updateData(id)
	cursor.execute(f"SELECT * FROM users WHERE userID = '{id}'")
	for userInfo in cursor.fetchall():
		userInfo = userInfo
	return userInfo

def addExp(startExp, nextLvlExp, id):
	cursor.execute(f"UPDATE users SET userExp = {startExp + nextLvlExp} WHERE userID = '{id}'")
	db.commit()

def updateAlias(id, alias):
	updateData(id)
	cursor.execute(f"UPDATE users SET useralias = '{alias}' WHERE userID = '{id}'")
	db.commit()

def removeAlias(id):
	updateData(id)
	cursor.execute(f"UPDATE users SET useralias = NULL WHERE userID = '{id}'")
	db.commit()

def removeLvl(id, lvl):
	updateData(id)
	cursor.execute(f"UPDATE users SET userlvl = {lvl} WHERE userID = '{id}'")
	db.commit()




def setup(client):
	client.add_cog(UserLvl(client))
