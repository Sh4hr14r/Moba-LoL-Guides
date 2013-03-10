import urllib2
from bs4 import BeautifulSoup
import re
import copy

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
##################################################Making BS4 Objects########################################################################
chsoup=BeautifulSoup(champions)
itsoup=BeautifulSoup(items)
absoup=BeautifulSoup(abilities)
##################################################Function Declarations#####################################################################
def name_dic_creator(soup,tag,attrib,pattern):
	"""Function for creating an empty dictionary containing the input soup's wanted names as keys."""	
	dic={}
	tags=[]
	for link in soup.find_all(tag,{attrib:pattern}):
		tags.append(link)
	for linktags in tags:
		dic[linktags.string]=None
	return dic
	
	
def link_tag_dic(soup,addr):
	"""Function for creating an empty dictionary containing the input soup's wanted names as keys."""
	dic={}
	tags=[]
	temptags=[]
	#Retrieving the desired information from the site 
	tags1 = [(td.find('a'),td.find('span')) for td in soup.find_all('td',{'class':'bg1-b'})]
	tags2 = [(td.find('a'),td.find('span')) for td in soup.find_all('td',{'class':'bg2-b'})]
	#Creating a temperory list containing the tags in order of appearance
	for j in range(2*len(atags1)):
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
		dic[sorted_tags[i][0].string]=[sorted_tags[i][0].get('href'),sorted_tags[i][1].string]
	return dic


#########################################################Creating The Names Dictionaries####################################################
Items=name_dic_creator(itsoup,'div','class','champ-name')
Champions=name_dic_creator(chsoup,'div','class','champ-name')
Abilities=link_tag_dic(absoup,'^http://www.mobafire.com/league-of-legends/ability/')
#########################################################Driver#############################################################################
print Abilities

