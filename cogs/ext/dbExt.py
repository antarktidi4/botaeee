import psycopg2, os


dbname = os.environ.get('dbname')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')

db = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = db.cursor()


def UI(user):
	cursor.execute(f"SELECT * FROM users WHERE userID = '{user.id}'")
	for userInfo in cursor.fetchall():
		return userInfo

def updateData(user):
	users = []
	cursor.execute(f"SELECT * FROM users")
	for dbUsers in cursor.fetchall():
		users.append(dbUsers[0])
	if str(user.id) not in users:
		cursor.execute(f"INSERT INTO users VALUES ('{user.id}', {0}, {1}, NULL)")
		db.commit()

def updateLvl(user, channel):
	userInfo = UI(user.id)
	exp = userInfo[1]
	lvlStart = userInfo[2]
	lvlEnd = int(exp ** (1/4))
	if lvlStart < lvlEnd:
		cursor.execute(f"UPDATE users SET userLvl = {lvlEnd} WHERE userID = '{user.id}'")
		db.commit()
		return f'{user.mention} up lvl {lvlEnd}'

def addExp(startExp, nextLvlExp, user):
	cursor.execute(f"UPDATE users SET userExp = {startExp + nextLvlExp} WHERE userID = '{user.id}'")
	db.commit()

def removeLvl(id, lvl):
	cursor.execute(f"UPDATE users SET userlvl = {lvl} WHERE userID = '{id}'")
	db.commit()

def updateAlias(id, alias):
	if alias is not None:
		cursor.execute(f"UPDATE users SET useralias = '{alias}' WHERE userID = '{id}'")
	else:
		cursor.execute(f"UPDATE users SET useralias = NULL WHERE userID = '{id}'")
	db.commit()
