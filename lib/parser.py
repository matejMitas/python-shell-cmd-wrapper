"""
Find, evaluate and parse blueprint files for commands
"""

"""
Generic library imports
"""
import os
import json
from pprint import pprint
from termcolor import colored
import jsonschema as js
"""
Functional imports
"""
import lib.defs as defs

class Parser:
	def __init__(self, path):
		self.path = path

		self.nesting_level = -1
		self.nest_key = None
		self.levels = []
	
	"""
	PUBLIC methods
	"""
	def parse(self):
		if self._check_blueprint_path():
			with open(self.path) as json_file:
				try:
					self.blueprint_file = json.load(json_file)
					"""
					Multiple libraries can be described in one file if 'settings' key
					is present on root level otherwise 
					"""
					self.no_of_libraries = 1

					if 'libraries' in self.blueprint_file['settings']:
						self.no_of_libraries = len(self.blueprint_file['settings']['libraries'])

					if self._check_blueprint():
						return True
				except ValueError as error:
					print(error)
					return False
		else:
			return False

	def get_flags(self):
		return self.blueprint_file['flags']

	def get_libraries(self):
		if self.no_of_libraries > 1:
			return self.blueprint_file['settings']['libraries']
		
	"""
	PRIVATE methods
	"""
	def _check_blueprint_path(self):
		"""
		Check correct file name is supplied and that file exists
		"""
		full_path = '{}/{}.json'.format(defs.BLUEPRINTS_PATH, self.path)
		if os.path.isfile(full_path):
			self.path = full_path
			return True
		else:
			return False

	def _check_blueprint(self):
		"""
		Validate general structure (flags list and settings)
		Schema can be found in defs.py
		"""
		try:
			js.validate(instance=self.blueprint_file, schema=defs.GENERAL_SCHEMA)
		except js.exceptions.ValidationError as expt:
			print(expt)
			return False
		"""
		Two schemas are defined, after checking general structure, each flags is 
		validated againts its schema
		"""
		for flag_key, flag_value in self.blueprint_file['flags'].items():
			if len(flag_value) != self.no_of_libraries:
				print('no')
				return False

			for flag in flag_value:
				try:
					js.validate(instance=flag, schema=defs.FLAG_SCHEMA)
				except js.exceptions.ValidationError as expt:
					print(expt)
		return True
			
