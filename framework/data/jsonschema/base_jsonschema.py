class BaseJSONSchema:

    def __init__(self):
        self.json_schema = {
            'type': 'object',
            'properties': {
                'headers': {
                    'type': 'object',
                    'properties': {
                        'Accept': {'enum': ['*/*']},
                        'Accept-Encoding': {'enum': ['gzip, deflate']},
                        'Connection': {'enum': ['close']},
                        'Host': {'enum': ['httpbin.org']},
                        'User-Agent': {'type': 'string'}
                    },
                    'additionalProperties': False
                }
            },
            'additionalProperties': False
        }
