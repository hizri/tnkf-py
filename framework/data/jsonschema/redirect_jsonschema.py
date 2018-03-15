from framework.data.jsonschema.base_jsonschema import BaseJSONSchema
from framework.utils.service_utils import log_built_schema


class RedirectJSONSchema(BaseJSONSchema):
    def __init__(self):
        super().__init__()
        self.json_schema['properties']['args'] = {'type': 'object'}
        self.json_schema['properties']['origin'] = {'type': 'string'}
        self.json_schema['properties']['url'] = {'enum': ['https://httpbin.org/get']}

    def build_redirect_schema(self):
        log_built_schema(self.json_schema)
        return self.json_schema
