class Ability:
	def __init__(self,ability_name):
		"""Initiation method for the ability object."""
		self.Name=ability_name
	def affiliation(self,champ_name):
		"""Method for setting the level of the spell."""
		self.Affiliation=champ_name
	def description(self,ability_desc):
		"""Method for setting a spell's description."""
		self.Description=ability_desc
