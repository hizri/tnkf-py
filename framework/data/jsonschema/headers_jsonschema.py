import json

from framework.utils.logger import logger


class HeadersJsonSchema:

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
                    }
                }
            },
            'additionalProperties': False
        }

    def build_headers_schema_default(self):
        self.json_schema['properties']['headers']['additionalProperties'] = False
        _log_built_schema(self.json_schema)
        return self.json_schema

    def build_headers_schema(self, headers):
        for key, value in headers.items():
            self.json_schema['properties']['headers']['properties'][key] = {'enum': [str(value)]}
        _log_built_schema(self.json_schema)
        return self.json_schema


def _log_built_schema(schema):
    schema = json.dumps(schema, indent=4)
    logger.debug('JSON schema was built:\n{}'.format(schema))
