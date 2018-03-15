import json

from framework.utils.logger import logger


class RedirectJSONSchema:

    def __init__(self):
        self.json_schema = {}

    def build_redirect_schema(self):
        self.json_schema = {
            'type': 'object',
            'properties': {
                'args': {'type': 'object'},
                'origin': {'type': 'string'},
                'url': {'enum': ['https://httpbin.org/get']},
                'headers': {
                    'type': 'object',
                    'properties': {
                        'Accept': {'enum': ['*/*']},
                        'Accept_Encoding': {'enum': ['gzip, deflate']},
                        'Connection': {'enum': ['close']},
                        'Host': {'enum': ['httpbin.org']},
                        'User-Agent': {'type': 'string'}
                    }
                }
            },
            'additionalProperties': False
        }
        _log_built_schema(self.json_schema)
        return self.json_schema


def _log_built_schema(schema):
    schema = json.dumps(schema, indent=4)
    logger.debug('JSON schema was built:\n{}'.format(schema))