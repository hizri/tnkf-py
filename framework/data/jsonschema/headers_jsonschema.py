from framework.data.jsonschema.base_jsonschema import BaseJSONSchema
from framework.utils.service_utils import log_built_schema


class HeadersJsonSchema(BaseJSONSchema):
    def __init__(self):
        super().__init__()

    def build_headers_schema_default(self):
        log_built_schema(self.json_schema)
        return self.json_schema

    def build_headers_schema(self, headers):
        for key, value in headers.items():
            self.json_schema['properties']['headers']['properties'][key.title()] = {'enum': [str(value)]}
        log_built_schema(self.json_schema)
        return self.json_schema
