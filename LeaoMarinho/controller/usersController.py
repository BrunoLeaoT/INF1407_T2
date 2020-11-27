from pymongo import MongoClient
from hashlib import sha256
database = 'mongodb+srv://bruno:br11do12@cluster0.iuukf.mongodb.net/test'
client = MongoClient(database)
db=client.inf1013

class UserController:
	def login(self,user,password):
		hashedPassword = sha256(password).hexdigest()
		user = db.users.find_one({"user":user,"password":hashedPassword})
		if user:
			return user
		return None
		
	def create(self,user,password):
		hashedPassword = sha256(password.encode('utf-8')).hexdigest()
		try:
			user = db.users.insert_one({"user":user,"password":hashedPassword})
			return True
		except:
			return False