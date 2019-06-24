"""
Business logic of the main module.
"""

"""
Generic library imports
"""

"""
Class imports
"""
from lib.parser import Parser
"""
Functional imports
"""
import lib.defs as defs

class Library:
	def __init__(self, blueprint_name, lib_name=None):
		"""
		Each blueprint can contain multiple libraries so further
		distinguishing needs to take place in form of lib_name providing
		actual name
		"""
		self.blueprint_name = blueprint_name
		self.lib_name = lib_name
		"""
		Fixed flags can only be set once 
		"""
		self.fixed_set = False
		"""
		Internal structure for storing flags
		"""
		self.structure = {
			'io'		: {
				'input'			: None,
				'output'		: None
			},
			'fixed'		: {
				'blueprint'		: {},
				'transformed'	: []
			},
			'variable'	: {
				'blueprint'		: {},
				'curr'			: 0
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

	def set_from_routine(self, json_file):
		pass

	def set_fixed(self, **kwargs):
		pass

	def set_variable(self, **kwargs):
		pass

	"""
	PRIVATE methods
	"""
	def _generate_io(self):
		return [self.structure['io']['input'], self.structure['io']['output']]

	def _get_blueprint(self):
		parser = Parser(self.blueprint_name)
		if not parser.parse():
			return 

		if parser.get_libraries():
			self.program_indexes = list(defs.LIBS.values())

		self.flags_match_table = parser.get_flags()

	def _transform_flag(self, opts):
		"""
		Take input flag and transform it to the desired format
		described in blueprint
		"""

	def _match_flag(self, flag):
		"""
		Find correct flag options in blueprint
		"""
