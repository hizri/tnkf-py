import pytest

from framework.checkers import response_check
from framework.data.jsonschema.headers_jsonschema import HeadersJsonSchema
from framework.helpers.generators import get_random_headers, get_random_string
from framework.service import httpbin


@pytest.allure.feature('Handler /headers')
class TestHeaders:

    @pytest.allure.story('Positive')
    def test_headers_default(self):
        """
        Handler /headers should return all request headers
        as JSON structure in response body.
        ===================================================
        Positive case with no custom headers in request.
        Default headers should be returned in response body.
        """
        code, headers, response = httpbin.request_headers()
        response_check.check_status_code_ok(code)
        response_check.validate_json_schema(response, HeadersJsonSchema().build_headers_schema_default())

    @pytest.allure.story('Positive')
    def test_headers_random_headers(self):
        """
        Handler /headers should return all request headers
        as JSON structure in response body
        ===================================================
        Positive case with random custom headers in request.
        Response headers should contain default and custom headers.
        """
        request_headers = get_random_headers()
        code, headers, response = httpbin.request_headers(request_headers)
        response_check.check_status_code_ok(code)
        response_check.validate_json_schema(response, HeadersJsonSchema().build_headers_schema(request_headers))

    @pytest.allure.story('Negative')
    @pytest.mark.parametrize('header_key',
                             ('\0', '\\n', '{} {}'.format(get_random_string(), get_random_string())),
                             ids=['empty', 'new line', 'space in key'])
    def test_headers_invalid_header_key(self, header_key):
        """
        Handler /headers should return all request headers
        as JSON structure in response body
        ===================================================
        Negative case with unexpected header keys in request.
        Response with 400 status code (Bad Request) should be returned.
        """
        request_headers = get_random_headers()
        request_headers[header_key] = get_random_string()
        code, *_ = httpbin.request_headers(request_headers)
        response_check.check_code_bad_request(code)
