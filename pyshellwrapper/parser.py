"""
Find, evaluate and parse blueprint files for commands
"""

"""
Generic library imports
"""
import os
import errno
import json
from pprint 		import pprint
from termcolor 		import colored
import jsonschema 	as js
"""
Functional imports
"""
import pyshellwrapper.defs 	as defs
import pyshellwrapper.utils 	as utils




class Parser:
	def __init__(self, file_type, json_file, possible_lib=None):
		self.type = file_type
		self.file = json_file
		self.lib = possible_lib
	
	"""
	PUBLIC methods
	"""
	def parse(self):
		self.data = self.handle_json()
		return getattr(self, '_parse_{}'.format(self.type))()
			


	@utils.check_method_validity(type=defs.BLUEPRINT)
	def get_flags(self):
		return self.data['flags']

	@utils.check_method_validity(type=defs.BLUEPRINT)
	def get_libraries(self):
		if self.no_of_libraries > 1:
			return self.data['settings']['libraries']

	@utils.check_method_validity(type=defs.ROUTINE)
	def get_fixed(self):
		pass

	@utils.check_method_validity(type=defs.ROUTINE)
	def get_variable(self):
		pass
		
	"""
	PRIVATE methods
	"""
	def handle_json(self):
		"""
		Used as a backbone function for handling
		blueprints and routines.
		"""
		paths = {
			'blueprint'	: defs.BLUEPRINTS_PATH,
			'routine'	: defs.ROUTINES_PATH
		}

		#print(self.type, self.file)

		if self.type not in list(paths.keys()):
			return None

		full_path = '{}/{}.json'.format(paths[self.type], self.file)
		if not os.path.isfile(full_path):
			raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), full_path)

		with open(full_path) as json_file:
			loaded_json = json.load(json_file)
			return loaded_json


	def _parse_blueprint(self):
		"""
		Multiple libraries can be described in one file if 'settings' key
		is present on root level otherwise 
		"""
		self.no_of_libraries = 1

		if 'libraries' in self.data['settings']:
			if self.lib not in self.data['settings']['libraries']:
				raise ValueError('Specified library \'{}\' not found in blueprint {}.json'.format(self.lib, self.file))
			self.no_of_libraries = len(self.data['settings']['libraries'])

		if self._check_blueprint():
			return True

	def _parse_routine(self):
		pass

	def _check_blueprint(self):
		"""
		Validate general structure (flags list and settings)
		Schema can be found in defs.py
		"""
		try:
			js.validate(instance=self.data, schema=defs.GENERAL_SCHEMA)
		except js.exceptions.ValidationError as expt:
			print(expt)
			return False
		"""
		'settings' enables to set required flags
		"""
		all_flags = list(self.data['flags'].keys())
		for required_flag in self.data['settings']['required_flags']:
			if required_flag not in all_flags:
				raise KeyError('Flag \'{}\' is required but not specified in \'flags\''.format(required_flag))
		

		"""
		Two schemas are defined, after checking general structure, each flags is 
		validated againts its schema
		"""
		for flag_key, flag_value in self.data['flags'].items():
			if len(flag_value) != self.no_of_libraries:
				raise ValueError('Supplied number of libraries {} does not match all listed variants for \'{}\''.format(self.no_of_libraries, flag_key))

			for flag in flag_value:
				"""
				Sometimes one might want to omit partical library's flag, while doing so supplied
				empty object is not valid according to the schema so it's skipped
				"""
				if flag:
					try:
						js.validate(instance=flag, schema=defs.FLAG_SCHEMA)
					except js.exceptions.ValidationError as expt:
						print(expt)
		return True

	def _check_routine(self):
		"""
		Validate general structure (fixed flags and variable flags)
		Schema can be found in defs.py
		"""
		pass
			
