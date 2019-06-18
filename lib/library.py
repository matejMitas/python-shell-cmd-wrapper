class Library:
	def __init__(self, blueprint_name, **kwargs):
		self.blueprint_name = blueprint_name

	def test(self):
		print(self.blueprint_name)