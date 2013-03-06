class Champion:
	"""This class is used for creating champion objects which can contain the data associated with a League of Legends champion 
	that is obtained from the MOBAFire website."""
	def __init__(self,champ_name):
		self.Name=champ_name
	
	def base_stats(self,health,hp_per_5,mana,mana_per_5,damage,attack_speed,armor,magic_resist,speed,champ_range,crit_chance=0):
		"""Method for setting a champion's base stats at level 1"""
		self.BsHealth=health
		self.BsHp5=hp_per_5
		self.BsMana=mana
		self.BsMp5=mana_per_5
		self.BsDamage=damage
		self.BsAS=attack_speed
		self.BsArmor=armor
		self.BsMagic_Resist=magic_resist
		self.BsSpeed=speed
		self.BsRange=champ_range
		self.BsCrit_Chance=crit_chance
		
	def base_stats18(self,health,hp_per_5,mana,mana_per_5,damage,attack_speed,armor,magic_resist,speed,champ_range,crit_chance=0):
		"""Method for setting a champion's base stats at level 18"""
		self.Bs18Health=health
		self.Bs18Hp5=hp_per_5
		self.Bs18Mana=mana
		self.Bs18Mp5=mana_per_5
		self.Bs18Damage=damage
		self.Bs18AS=attack_speed
		self.Bs18Armor=armor
		self.Bs18Magic_Resist=magic_resist
		self.Bs18Speed=speed
		self.Bs18Range=champ_range
		self.Bs18Crit_Chance=crit_chance
	
	def base_stats_change(self,health,hp_per_5,mana,mana_per_5,damage,attack_speed,armor,magic_resist,crit_chance):
		"""Method for setting a champion's base stats changes for each level-up."""
		self.Health_Plus=health
		self.Hp5_Plus=hp_per_5
		self.Mana_Plus=mana
		self.Mp5_Plus=mana_per_5
		self.Damage_Plus=damage
		self.AS_Plus=attack_speed
		self.Armor_Plus=armor
		self.Magic_Resist_Plus=magic_resist
		self.Crit_Chance_Plus=crit_chance
	
	def role(self,roles=[]):
		"""Method for setting a champion's role in the game."""
		self.Roles=roles
	def spells(self,spells={}):
		"""Method for setting a champion's spells by using a dictionary containing Spell objects of the champion"""
		self.Spells=spells
	def price(self,rp,ip):
		"""Method for setting a champion's Riot Point and Influence Point prices."""
		self.RP_Price=rp
		self.IP_Price=ip
