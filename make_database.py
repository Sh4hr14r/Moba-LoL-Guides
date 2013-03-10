'''
	here we put we give an object to the class and after that we can use 
	Add_to_database function to put thing or information in the database.
'''
import pymongo
class database(object):
	def __init__(self,Object):
		self.post = Object
		self.conn = pymongo.Connection()
		self.db = self.conn['mobafire']
		self.db['collect1']
		
	def Add_to_database(self,self.post.__dict__):
		'''adding infomations to database'''
		self.db.collect1.insert(self.post.__dict__)
