'''
	here we put we give an object to the class and after that we can use 
	Add_to_database function to put thing or information in the database.
'''
import pymongo


def make_database(dic):
	''' this function try to make database'''
	conn = pymongo.Connection()
	db = conn["Mobafire"]
	db["League of Legends"]
	
	
