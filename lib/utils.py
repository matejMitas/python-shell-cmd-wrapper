"""
Functions used throught the program.
"""

"""
Generic library imports
"""
import os
import json

"""
Functional imports
"""
import lib.defs 	as defs

def handle_json_file(file_type, file_name):
	"""
	Used as a backbone function for handling
	blueprints and routines.

	:param file_type: open files from blueprint directory or 
					  from routines directory
	:type  file_type: str
	:param file_path: name of file in question without 
					  complete path, it gets resolved from
					  first param
	:type  file_path: str
	"""
	paths = {
		'blueprint'	: defs.BLUEPRINTS_PATH,
		'routine'	: defs.ROUTINES_PATH
	}

	if file_type not in list(paths.keys()):
		return None

	full_path = '{}/{}.json'.format(paths[file_type], file_name)
	if not os.path.isfile(full_path):
		return None

	with open(full_path) as json_file:
		try:
			loaded_json = json.load(json_file)
			return loaded_json
		except ValueError as error:
			print(error)
			return None