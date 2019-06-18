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
"""
Functional imports
"""
import lib.defs as defs

class Parser:
	def __init__(self, path):
		self.path = path

		self.semantics = {
			'required': [
				['flags']
			],
			'optional': [
				['settings']
			]
		}

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
					self._check_blueprint()
					return True
				except ValueError as error:
					print(error)
					return False
		else:
			return False
		
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
		self._get_indexes_json(self.blueprint_file)
		pprint(self.levels)

	def _get_indexes_json(self, entry=None):
		"""
		Each invokation increases nesting level
		"""
		self.nesting_level += 1
		"""
		Loop through whole tree until atomic values are reached
		"""
		for key in entry:
			"""
			Add key to corresponding level
			"""
			try:
				self.levels[self.nesting_level]
			except IndexError:
				self.levels.append([])

			ptr = self.levels[self.nesting_level]
			if key not in ptr:
				ptr.append(key)

			print('{} - {}{}'.format(self.nesting_level, '\t'*(self.nesting_level), key))
			self.nest_key = key
			try:
				l = entry[key]
				if type(l) == dict:
					self._get_indexes_json(l)
				elif type(l) == list:
					for item in l:
						if self._is_primitive(item):
							pass
							print('{}{}'.format('\t'*(self.nesting_level+1), item))
						else:
							self._get_indexes_json(item)
				else:
					pass
					print('{}{} - {}'.format('\t'*(self.nesting_level+1), l, self.nest_key))
			except TypeError:
				pass
		"""
		After each recursively invoked loop nesting level counter
		must be decremeted to allow for correct leveling
		"""
		self.nesting_level -= 1

	def _is_primitive(self, value):
		primitives = (str, bool, float, int)
		return True if type(value) in primitives else False
			
