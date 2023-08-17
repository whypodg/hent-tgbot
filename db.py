import json
import sqlite3


class DataBase():
	def __init__(self, filename: str = "db.db"):
		self.db = sqlite3.connect(filename)
		self.cursor = self.db.cursor()


	def getConfig(self, key):
		with open("config.json", "r", encoding='utf-8') as f:
			data = json.loads(f.read())

		return data.get(key, None)


	def recvs(self, f):
		self.cursor.execute(f)
		return self.cursor.fetchall()

	def save(self, f):
		self.cursor.execute(f)
		return self.db.commit()


	def regUser(self, uid: int, as_dict: bool = False):
		u = self.getUser(uid, as_dict)
		if not u:
			self.save(f"""INSERT INTO users (id) VALUES ({uid})""")
			u = self.getUser(uid, as_dict)
		return u

	def getUser(self, uid: int, as_dict: bool = False):
		user = self.recvs(f"SELECT * FROM users WHERE id = {uid}")
		us = None if len(user) == 0 else user[0]
		if as_dict and us:
			us = {
				"id": us[0],
				"status": us[1]
			}
		return us

	def getAllUsers(self):
		return self.recvs(f"SELECT * FROM users")