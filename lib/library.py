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
		
		return output_buffer

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
		for flag, opts in kwargs.items():
			flag_blueprint = self._match_flag(flag)
			"""
			First thing to decide is whenever single or more values
			were supplied
			"""
			items_count = flag_blueprint['format']['count']
			"""
			Check for easiest case, only one primitive value 
			"""
			if self._is_primitive(opts):
				print(self._transform_flag(flag_blueprint, opts))
			else:
				"""
				Tuple is single value, list means more expansion.
				But tuple can be nested.
				"""
				if type(opts) == tuple:
					"""
					Nested tuple, flag with list option
					"""
					if type(opts[0]) == tuple:
						"""
						TODO: address list in next version
						"""
						pass
					else:
						print(self._transform_flag(flag_blueprint, opts))
				else:
					for opt in opts:
						print(self._transform_flag(flag_blueprint, opt))

			print()
			
			



	"""
	PRIVATE methods
	"""
	def _set_variable_single(self, flag_blueprint, opts):
		if items_count > 1:
				"""
				Multiple values, can be in nested list
				"""
				print('multiple')

		else:
			"""
			Value is primitive data type, assign can take place
			"""
			pass
			#print(opts)
			#print(self._transform_flag(flag_blueprint, opts))
			#print('single')


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
		opts_preset_type = type(opts_preset)

		
		if opts_preset_type == str:
			"""
			String means matching of predefined presets
			"""
			if opts_preset == '1':
				return opts
			else:
				return defs.FORMAT_OPTIONS[opts_preset].format(opts[0], opts[1])
		elif opts_preset_type == dict:
			"""
			Custom formating is also enabled, setting divider/left & right side of expression
			"""
			print(opts_preset)
			return '{}{}{}{}{}'.format(opts_preset['left'], opts[0], opts_preset['divider'], opts[1], opts_preset['right'])


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

	def _is_primitive(self, item):
		if type(item) not in [list, tuple, dict]:
			return True
		else:
			return False
			