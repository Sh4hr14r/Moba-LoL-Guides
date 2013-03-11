class Rune:
	def __init__(self,rune_name):
		"""Initiation method for the rune object."""
		self.Name=rune_name
		
	def tier(self,tier):
		"""Method for setting the tier of rune objects."""
		self.Tier=tier
	
	def description(self,rune_desc):
		"""Method for setting a rune's description."""
		self.Description=rune_desc
	
	def type(self,kind):
		"""Method for setting a rune's type;eg:Mark,Seal,..."""
		self.Variety=kind
