# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
from Spell import Spell
from Ability import Ability
from Item import Item
from Add_Database import *
#champ_url='http://www.mobafire.com/league-of-legends/champions'
#champ_resp=urllib2.urlopen(champ_url)
#champions=champ_resp.read()
##################################################Opening The Needed Files##################################################################
champ_resp=open("/home/shahriar/Desktop/Mobafire/League of Legends Strategy Build Guide :: LoL Strategy Building Tool by MOBAFire.html",'r')
champions=champ_resp.read()
item_resp=open("/home/shahriar/Desktop/Mobafire/Items.html",'r')
items=item_resp.read()
ability_resp=open("/home/shahriar/Desktop/Mobafire/Abilities.html",'r')
abilities=ability_resp.read()
spell_resp=open("/home/shahriar/Desktop/Mobafire/Spells.html",'r')
spells=spell_resp.read()
##################################################Making BS4 Objects########################################################################
chsoup=BeautifulSoup(champions)
itsoup=BeautifulSoup(items)
absoup=BeautifulSoup(abilities)
spsoup=BeautifulSoup(spells)
##################################################Function Declarations#####################################################################
def name_dic_creator(soup):
	"""Function for creating an empty dictionary containing the input soup's wanted names as keys."""	
	dic={}
	tags=[(a,a.find('div',{'class':'champ-name'}),a.find('div',{'class':'champ-sub'})) for a in soup.find_all('a',{'class':'champ-box'})]
	for i in range(len(tags)):
		dic[tags[i][1].string]=[tags[i][0].get('href'),tags[i][2].text.strip()]
	return dic

	
def link_tag_dic(soup):
	"""Function for creating an empty dictionary containing the input soup's wanted names as keys."""
	dic={}
	tags=[]
	temptags=[]
	#Retrieving the desired information from the site 
	tags1 = [(td.find('a'),td.find('span')) for td in soup.find_all('td',{'class':'bg1-b'})]
	tags2 = [(td.find('a'),td.find('span')) for td in soup.find_all('td',{'class':'bg2-b'})]
	#Creating a temperory list containing the tags in order of appearance
	for j in range(2*len(tags1)):
		if j%2==0:
			temptags.append(tags2[j/2])
		else:
			temptags.append(tags1[j/2])
	#Ommiting the tuples containing None Type elements from the list
	for link in temptags:
		if link[0]!=None and link[1]!=None:
			tags.append(link)
	#Sorting the tags list by using the name of the abilities for the future if the need rises
	sorted_tags=sorted(tags,key=lambda x:tags[tags.index(x)][0].string)
	#Creating the desired dictionary containing ability names and their links and descriptions.
	for i in range(len(sorted_tags)):
		dic[sorted_tags[i][0].text.strip()]=[sorted_tags[i][0].get('href'),sorted_tags[i][1].string]
	return dic


def spells_class_dic(dic):
	"""Function for setting the values of spells in a spell object attributes and putting them into that dictionary."""
	for a in dic.keys():
		exec(a+"=Spell(a)")
		exec(a+".Description = dic[a][1]")
		exec("dic[a].append("+a+")")
	return dic


def abilities_class_dic(dic):
	"""Function for setting the values of abilities in a ability object attributes and putting them into that dictionary."""
	for a in dic.keys():
		temp=a.strip()
		temp=temp.replace(':','')
		temp=temp.replace("'",'_')
		temp=temp.replace("-",'_')
		temp=temp.replace(' ','_')
		temp=temp.replace("/","OR")
		temp=temp.replace(",","_")
		temp=temp.replace("90","Ninety")
		temp=temp.replace("!","")
		exec(temp+" = Ability(a)")
		exec(temp+".Description = dic[a][1]")
		exec("dic[a].append("+temp+")")
	return dic
	
	
def create_final(dic,ind):
	"""Generating the final Object dictionary for using in the desired database."""
	for a in dic.keys():
		dic[a]=dic[a][ind].__dict__
	return dic


def item_class_creator(dic):
	"""Function for setting the values of the Item objects attributes and putting them into that dictionary."""
	for a in dic.keys():
		item_resp=urllib2.urlopen(dic[a][0])
		item=item_resp.read()
		itemsoup=BeautifulSoup(item)
		tags=[div.find_all('p') for div in itemsoup.find_all('div',{'class':'item-info float-left'})]
		dic[a].append(tags[0][2].text.strip())
		temp=a.strip()
		temp=temp.replace(':','')
		temp=temp.replace("'",'_')
		temp=temp.replace("-",'_')
		temp=temp.replace(' ','_')
		temp=temp.replace("/","OR")
		temp=temp.replace(",","_")
		temp=temp.replace("!","")
		temp=temp.replace(".","")
		exec(temp+" = Item(a)")
		exec(temp+".Description = dic[a][2]")
		exec(temp+".Price = dic[a][1]")
		exec("dic[a].append("+temp+")")
	return dic


def make_db(dic,db,field):
	"""Function for creating the database"""
	for i in dic.keys():
		Add_Field(dic[i],db,field)


#########################################################Creating The Names Dictionaries####################################################
Items=name_dic_creator(itsoup)
#Champions=name_dic_creator(chsoup,'div','class','champ-name')
Abilities=link_tag_dic(absoup)
Spells=link_tag_dic(spsoup)
#########################################################Completed Dictionaries#############################################################
Spells=create_final(spells_class_dic(Spells),2)
Abilities=create_final(abilities_class_dic(Abilities),2)
Items=create_final(item_class_creator(Items),3)
##########################################################Making a connection###############################################################
database=get_connection()
##########################################################Creating the databases############################################################
make_db(Abilities,database,'Abilities')
make_db(Items,database,'Items')
make_db(Spells,database,'Spells')
#########################################################Driver#############################################################################

