"""
Find, evaluate and parse blueprint files for commands
"""

"""
Generic library imports
"""
import os

"""
Class imports
"""

"""
Functional imports
"""



class Parser:
	def __init__(self, path):
		self.path = path
	
	"""
	PUBLIC methods
	"""
	def parse(self):
		self._check_blueprint()
		"""
		with open(self.path) as json_file:
			try:
				self.json_file = json.load(json_file)
				return True
			except ValueError as error:
				print(error)
		"""

	"""
	PRIVATE methods
	"""
	def _check_blueprint(self):
		print(os.path.isfile('./blueprint/compress_libs.json'))