class Spell:
	def __init__(self,spell_name):
		"""Initiation method for the spell object."""
		self.Name=spell_name
	def affiliation(self,champ_name):
		"""Method for setting the ownership of the spell objects."""
		self.Affiliation=champ_name
	def description(self,spell_desc):
		"""Method for setting a spell's description."""
		self.Description=spell_desc
