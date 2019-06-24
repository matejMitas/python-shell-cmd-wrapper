"""
Definitions used throught the program.
"""

BLUEPRINT = 'blueprint'
ROUTINE = 'routine'

BLUEPRINTS_PATH = './{}'.format(BLUEPRINT)
ROUTINES_PATH 	= './{}'.format(ROUTINE)



FORMAT_OPTIONS = {
	'single'		: '{}',
	'pair'			: '{},{}',
	'pair_braces'	: '{{{},{}}}',
	'pair_box'		: '[{},{}]',
	'match'			: None,
	'toggle'		: None	
}

"""
General flags blueprint 
"""
GENERAL_SCHEMA = {
	'$schema'				: 'http://json-schema.org/schema#',
	'type'					: 'object',
	'additionalProperties'	: False,
	'required'				: ['settings', 'flags'],
	'properties'			: {
		'settings' : {
			'type' 		 : 'object',
			'additionalProperties'	: False,
			'required'	 : ['required_flags'],
			'properties' : {
				'required_flags': {
					'type': 'array'
				},
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

"""
Flag schema
"""
FLAG_SCHEMA = {
	'type':'object',
	'required':[  
	    'flag',
	    'unifier',
	    'format'
	],
	'additionalProperties':False,
	'properties':{  
	    'flag':{  
	        'type':[  
	            'null',
	            'string'
	        ]
	    },
	    'unifier':{  
	        'type':[  
	            'null',
	            'string'
	        ]
	    },
	    'format':{  
	        'type':'object',
	        'dependencies': {
			    'match': ['pattern']
			},
	        'properties':{  
	            'format':{  
	                'type':'string',
	                'pattern':'|'.join(['({})'.format(i) for i in list(FORMAT_OPTIONS.keys())])
	            },
	            'list':{  
	                'type':'object',
	                'properties':{  
	                    'divider':{  
	                        'type':'string'
	                    }
	                }
	            },
	            'pattern': {},
	            'match': {
	            	'type': 'boolean'
	            },
	            'toggle': {
	            	'type': 'boolean'
	            }
	        }
	    }
	}
}