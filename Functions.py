import urllib2
from bs4 import BeautifulSoup

#champ_url='http://www.mobafire.com/league-of-legends/champions'
#champ_resp=urllib2.urlopen(champ_url)
#champions=champ_resp.read()
champ_resp=open("/home/shahriar/Desktop/Mobafire/League of Legends Strategy Build Guide :: LoL Strategy Building Tool by MOBAFire.html",'r')
champions=champ_resp.read()
item_resp=open("/home/shahriar/Desktop/Mobafire/Items.html",'r')
items=item_resp.read()

chsoup=BeautifulSoup(champions)
itsoup=BeautifulSoup(items)
def champ_dic(soup,pattern):
	"""Function for creating an empty dictionary containing the input soup's wanted names as keys."""	
	dic={}
	tags=[]
	for link in soup.find_all('div',{'class':pattern}):
		tags.append(link)
	for linktags in tags:
		dic[linktags.string]=None
	return dic

Items=champ_dic(itsoup,'champ-name')
Champions=champ_dic(chsoup,'champ-name')
print Items.keys()
print '#######################################################################'
print Champions.keys()
print len(Items)
print len(Champions)
