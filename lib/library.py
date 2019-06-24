"""
Business logic of the main module.
"""

"""
Generic library imports
"""
from pprint import pprint
"""
Class imports
"""
from lib.parser import Parser
"""
Functional imports
"""
import lib.defs as defs

class Library:
	def __init__(self, blueprint, lib=None, **kwargs):
		"""
		Each blueprint can contain multiple libraries so further
		distinguishing needs to take place in form of lib_name providing
		actual name
		"""
		self.blueprint_name = blueprint
		self.lib_name = lib
		"""
		Fixed flags can only be set once 
		"""
		self.fixed_set = False
		"""
		Internal structure for storing flags
		"""
		self.structure = {
			'fixed'		: {
				'original'		: {},
				'transformed'	: []
			},
			'variable'	: {
				'original'		: {},
				'transformed'	: []
			}
		}

		"""
		Fetch correct blueprint for command 
		"""
		self._get_blueprint()

	"""
	PUBLIC methods
	"""
	def reset(self):
		"""
		Resets
		"""
		self.fixed_set = False

	def construct(self):
		"""
		Transform abstract data structure to list used by subprocess 
		"""
		output_buffer = []
		"""
		Add constant flags and items
		"""
		output_buffer += [self.lib_name if self.lib_name else self.blueprint_name]
		
		return {
			'index': 0,
			'items': []
		}

	def set_from_routine(self, routine_file):
		parser = Parser('routine', routine_file)

		pass

	def set_fixed(self, **kwargs):
		for flag, opt in kwargs.items():
			print(flag, opt)
			print(self._match_flag(flag))
			print()

	def set_variable(self, **kwargs):
		pass

	"""
	PRIVATE methods
	"""
	def _get_blueprint(self):
		parser = Parser('blueprint', self.blueprint_name, self.lib_name)
		if not parser.parse():
			return False
		"""
		If there are multiple libraries in blueprint correct index of 
		library must be found to later enable addressing of flag opts
		"""
		self.program_indexes = parser.get_libraries()
		if not self.program_indexes:
			self.blueprint_index = 0
		else:
			self.blueprint_index = self.program_indexes.index(self.lib_name)
		"""
		Get all flags/opts from file
		"""
		self.flags_match_table = parser.get_flags()
		if not self.flags_match_table:
			raise ValueError()

		return True

	def _transform_flag(self, opts):
		"""
		Take input flag and transform it to the desired format
		described in blueprint
		"""

	def _match_flag(self, flag):
		"""
		Find correct flag options in blueprint
		"""
		full_flag = '@{}'.format(flag)
		print(full_flag)
		print(self.flags_match_table[full_flag][0])
		
