from random import randint

import pytest

from framework.checkers import response_check
from framework.data.jsonschema.redirect_jsonschema import RedirectJSONSchema
from framework.helpers.generators import get_random_string
from framework.service import httpbin


@pytest.allure.feature('Handler /redirect')
class TestRedirect:

    @pytest.allure.story('Positive')
    def test_redirect(self):
        """
        /redirect/:N handler should make N redirects before response is returned
        ========================================================
        Positive case with random valid redirects count
        """
        count = randint(1, 10)
        code, _, history, response = httpbin.request_redirect(count)
        response_check.check_status_code_ok(code)
        response_check.check_redirect_count(history, count)
        response_check.validate_json_schema(response, RedirectJSONSchema().build_redirect_schema())

    @pytest.allure.story('Negative')
    @pytest.mark.parametrize('invalid_count', [-1 * randint(1, 200), get_random_string(), ''],
                             ids=['negative int', 'random string', 'empty'])
    def test_redirect_wrong_count(self, invalid_count):
        """
        /redirect/:N handler should make N redirects before response is returned
        ========================================================
        Negative case with random invalid redirects count value
        Response with 404 status code (Not Found) should be returned
        """
        code, _, history, response = httpbin.request_redirect(invalid_count)
        response_check.check_code_not_found(code)
