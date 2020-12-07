from discord.ext import commands
import discord, psycopg2, os


dbname = os.environ.get('dbname')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


db = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = db.cursor()


class UserLvl(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
		await updateData(member)


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot is False:

			await updateData(message.author)

			cursor.execute(f"SELECT userExp FROM users WHERE userID = '{message.author.id}'")
			for userInfo in cursor.fetchall():
				uExp = userInfo[0]
			cursor.execute(f"UPDATE users SET userExp = {uExp + 5} WHERE userID = '{message.author.id}'")
			db.commit()

			await updateLvl(message.author, message.channel)


async def updateData(user):
	u = []
	cursor.execute(f"SELECT * FROM users")
	for dbUsers in cursor.fetchall():
		u.append(dbUsers[0])
	if str(user.id) not in u:
		cursor.execute(f"INSERT INTO users VALUES ('{user.id}', {0}, {1})")
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
	cursor.execute(f"SELECT * FROM users WHERE userID = '{id}'")
	for userInfo in cursor.fetchall():
		userInfo = userInfo
	return userInfo

def addExp(startExp, nextLvlExp, id):
	cursor.execute(f"UPDATE users SET userExp = {startExp + nextLvlExp} WHERE userID = '{id}'")
	db.commit()


	

def setup(client):
	client.add_cog(UserLvl(client))
