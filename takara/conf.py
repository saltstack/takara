CLI_CONFIG = {
        'unit': {
            'options': ['-u'],
            'default': 'main',
            'sub': ['create', 'get', 'set'],
            'help': 'The unit to work with, if empty the unit "main" is used'
            },
        'store': {
            'default': 'file',
            'sub': ['create', 'get', 'set'],
            'help': 'Chose the storage medium to use',
            },
        'cipher': {
            'options': ['-C'],
            'default': 'fernet',
            'sub': 'create',
            'help': 'When creating or cipher to use for storage of data for the new unit',
            },
        'seal': {
            'options': ['-S'],
            'default': 'passwd',
            'sub': 'create',
            'help': 'The type of seal to use to secure the storage interface',
            },
        'path': {
            'options': ['-p'],
            'default': None,
            'sub': ['set', 'get'],
            'help': 'The path to store or retrive the desired data',
            },
        'string': {
            'options': ['-s'],
            'defalt': None,
            'sub': 'set',
            'help': 'Choose a string to set as the value for the given storage path',
            },
        'file': {
            'options': ['-f'],
            'default': None,
            'sub': 'set',
            'help': 'Choose a local file to set as the value to find for the given path',
            },
        'data_dir': {
            'default': '/var/takara/data',
            'sub': ['create', 'set', 'get'],
            'help': 'The directory to store data specific to the configuration of encrypted units when using local file storage systems',
            },
        'unit_dir': {
            'default': '/var/takara/unit',
            'sub': ['create', 'set', 'get'],
            'help': 'The directory to store encrypted data when using the local file storage system'
            },
        }
CONFIG = {}
GLOBAL = {}
SUBS = {
        'create': {
            'desc': 'Create New Units',
            'help': 'Use create to make new units to store encrypted data',
            },
        'set': {
            'desc': 'Set data to a location',
            'help': 'Use set to change or add a location for a given unit',
            },
        'get': {
            'desc': 'Get data from a location',
            'help': 'Use Get to retrive data from a given location',
            },
        }
DYNE = {
        'takara': ['takara'],
        }
