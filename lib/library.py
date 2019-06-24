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
		Add command
		"""
		output_buffer += [self.lib_name if self.lib_name else self.blueprint_name]
		"""
		Add fixed
		"""
		output_buffer += self.structure['fixed']['transformed']
		
		print(output_buffer)

		return {
			'index': 0,
			'items': []
		}

	def set_from_routine(self, routine_file):
		parser = Parser('routine', routine_file)

		pass

	def set_fixed(self, **kwargs):
		for flag, opts in kwargs.items():
			"""
			Backup for possible repeated use
			"""
			self.structure['fixed']['original'][flag] = opts
			"""
			Find corresponding partition of the blueprint and 
			transform flag accordingly 
			"""
			flag_blueprint = self._match_flag(flag)
			self.structure['fixed']['transformed'] += self._transform_flag(flag_blueprint, opts)


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

	def _transform_flag(self, flag_blueprint, opts):
		"""
		Take input flag and transform it to the desired format
		described in blueprint
		"""
		transform_buffer 		= []
		"""
		Mandatory parts of blueprint as local variable for 
		more readable code
		"""
		flag 		= flag_blueprint['flag']
		unifier 	= flag_blueprint['unifier']
		opt_format 	= flag_blueprint['format'] 
		"""
		Opts are the most important part of the transformation because
		they need to put into the right format or even concatenated to
		a list hence they are first to address
		"""
		if 'list' in flag_blueprint['format']:
			transformed_opt = None
		else:
			transformed_opt = self._transform_opts(flag_blueprint['format'], opts)


		if transformed_opt:
			"""
			Handle unifier
			"""		
			if unifier:
				transform_buffer.append('{}{}{}'.format(flag, unifier, transformed_opt))
			else:
				"""
				Handle flag
				"""
				if flag:
					transform_buffer.append(flag)
				transform_buffer.append(transformed_opt)
		
		return transform_buffer


	def _transform_opts(self, opts_blueprint, opts):
		opts_preset = opts_blueprint['preset']

		if opts_preset == '1':
			return opts

		# print(opts_blueprint)
		# print(opts)

	def _transform_opts_list(self, opts_blueprint, opts):
		pass

	def _match_flag(self, flag):
		"""
		Find correct flag options in blueprint
		"""
		try:
			return self.flags_match_table[flag][self.blueprint_index]
		except KeyError:
			raise KeyError('flag \'{}\' is not available in current blueprint. You can either try different blueprint or create new one'.format(flag))
		