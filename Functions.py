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
	tdtags=[]
	atags=[]
	tempatags=[]
	spantags=[]
	atags1 = [td.find('a') for td in soup.find_all('td',{'class':'bg1-b'})]
	atags2 = [td.find('a') for td in soup.find_all('td',{'class':'bg2-b'})]
	atags1=set(atags1)
	atags1=list(atags1)
	atags1.remove(None)
	atags2=set(atags2)
	atags2=list(atags2)
	atags2.remove(None)
	for j in range(2*len(atags1)):
		if j%2==0:
			tempatags.append(atags2[j/2])
		else:
			tempatags.append(atags1[j/2])
	spantags1 = [td.find('span') for td in soup.find_all('td',{'class':'bg1-b'})]
	spantags2 = [td.find('span') for td in soup.find_all('td',{'class':'bg2-b'})]
	spantags1=set(spantags1)
	spantags1=list(spantags1)
	spantags1.remove(None)
	spantags2=set(spantags2)
	spantags2=list(spantags2)
	spantags2.remove(None)
	for j in range(2*len(spantags1)):
		if j%2==0:
			spantags.append(spantags2[j/2])
		else:
			spantags.append(spantags1[j/2])
	for link in tempatags:
		if link.string!=None:
			atags.append(link)
	sorted_atags=sorted(atags,key=lambda x:atags[atags.index(x)].string)
	for i in range(len(sorted_atags)):
		dic[sorted_atags[i].string]=[sorted_atags[i].get('href'),spantags[i].string]
	return dic


#########################################################Creating The Names Dictionaries####################################################
Items=name_dic_creator(itsoup,'div','class','champ-name')
Champions=name_dic_creator(chsoup,'div','class','champ-name')
Abilities=link_tag_dic(absoup,'^http://www.mobafire.com/league-of-legends/ability/')
#########################################################Driver#############################################################################
print Abilities

