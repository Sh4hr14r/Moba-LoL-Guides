import pymongo
################## GETING CONNECTION
conn = pymongo.Connection()
db = conn["MOBAFIRE"]
######### making Spells field
######### making Item field
######### making Champion field	  ====>>>{all of Fields in under League of legend}
######### making Abilities field
######### making Runes field
######### making League of Legends
def Add_Spells(dic):
	db.League_Of_Legend.Spells.insert(dic)
def Add_Item(dic):
	db.League_Of_Legend.Item.insert(dic)
def Add_champions(dic):
	db.League_Of_Legend.Champions(dic)
def Add_Abilities(dic):	
	db.League_Of_Legend.Abilities(dic)
def Add_Runes(dic):
	db.League_Of_Legend.Runes(dic)
	
