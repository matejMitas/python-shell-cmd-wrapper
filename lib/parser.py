"""
Find, evaluate and parse blueprint files for commands
"""

"""
Generic library imports
"""
import os
import json
from pprint 		import pprint
from termcolor 		import colored
import jsonschema 	as js
"""
Functional imports
"""
import lib.defs 	as defs
import lib.utils 	as utils

class Parser:
	def __init__(self, blueprint_name):
		self.blueprint_name = blueprint_name

		self.nesting_level = -1
		self.nest_key = None
		self.levels = []
	
	"""
	PUBLIC methods
	"""
	def parse(self):
		self.blueprint = utils.handle_json_file('blueprint', self.blueprint_name)
		"""
		Multiple libraries can be described in one file if 'settings' key
		is present on root level otherwise 
		"""
		self.no_of_libraries = 1

		if 'libraries' in self.blueprint['settings']:
			self.no_of_libraries = len(self.blueprint['settings']['libraries'])

		if self._check_blueprint():
			return True

	def get_flags(self):
		return self.blueprint['flags']

	def get_libraries(self):
		if self.no_of_libraries > 1:
			return self.blueprint['settings']['libraries']
		
	"""
	PRIVATE methods
	"""
	def _check_blueprint(self):
		"""
		Validate general structure (flags list and settings)
		Schema can be found in defs.py
		"""
		try:
			js.validate(instance=self.blueprint, schema=defs.GENERAL_SCHEMA)
		except js.exceptions.ValidationError as expt:
			print(expt)
			return False
		"""
		Two schemas are defined, after checking general structure, each flags is 
		validated againts its schema
		"""
		for flag_key, flag_value in self.blueprint['flags'].items():
			if len(flag_value) != self.no_of_libraries:
				print('no')
				return False

			for flag in flag_value:
				try:
					js.validate(instance=flag, schema=defs.FLAG_SCHEMA)
				except js.exceptions.ValidationError as expt:
					print(expt)
		return True
			
