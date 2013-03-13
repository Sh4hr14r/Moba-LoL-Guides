# -*- coding: utf-8 -*-
import pymongo
################## GETING CONNECTION
def get_connection():
	"""Function for seting up a connection."""
	conn = pymongo.Connection()
	db = conn["League_Of_Legend"]
	return db

############################################
def Add_Field(dic,db,Field):
	try:
		exec("db.League_Of_Legend."+Field+".insert(dic)")
	except:
		print dic
		print type(dic)
