class Spell:
	def __init__(self,spell_name):
		"""Initiation method for the spell object."""
		self.Name=spell_name

	def level(self,level):
		"""Method for setting the level of the spell."""
		self.Level=level

	def description(self,spell_desc):
		"""Method for setting a spell's description."""
		self.Description=spell_desc
