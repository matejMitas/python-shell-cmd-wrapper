"""
Definitions used throught.
"""

BLUEPRINTS_PATH = './blueprint'

GENERAL_SCHEMA = {
	'$schema'				: 'http://json-schema.org/schema#',
	'type'					: 'object',
	'additionalProperties'	: False,
	'required'				: ['flags'],
	'properties'			: {
		'settings' : {
			'type' 		 : 'object',
			'required'	 : ['libraries'],
			'properties' : {
				'libraries': {
					'type'	: 'array'
				}
			}
		},
		'flags' : {
			'type' 		 : 'object'
		}
	}
}

FLAG_SCHEMA = {
	'type': 'object',
	'properties': {
		'flag': {
			'type'		: 'string'
		}, 
		'unifier': {
			'type'		: ['null', 'string']
		},
		'format': {
			'type'		: 'string'
		}
	},
	'required': ['flag', 'unifier', 'format']
}