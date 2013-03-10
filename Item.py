class item:
	def __init__(self,item_name):
		""" The initiation method."""
		self.Name=item_name
	def price(self,price):
		"""Method for setting an item's price."""
		self.Price=price
	def type(self,variety=None):
		"""Method for defining an item's type."""
		self.Variety=variety
	def description(self,item_desc):
		"""Method for setting a item's description."""
		item.Description=item_desc
