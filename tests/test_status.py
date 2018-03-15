from random import randint

import pytest

from framework.checkers import response_check
from framework.helpers.generators import get_random_string
from framework.service import httpbin


@pytest.allure.feature('Handler /status')
class TestStatus:

    @pytest.allure.story('Positive')
    def test_status(self):
        """
        Handler /status/{code} should return response with same status code as was sent
        as request parameter. Valid code should be 3-digit value
        ========================================================
        Positive case with random valid status code value (3-digit number)
        """
        status_code = randint(110, 999)
        code, *_ = httpbin.request_status(status_code)
        response_check.check_status_code_matches_expected(code, status_code)

    @pytest.allure.story('Negative')
    def test_status_empty_value(self):
        """
        Handler /status/{code} should return response with same status code as was sent
        as request parameter. Valid code should be 3-digit value
        ========================================================
        Negative case with no status code value in request.
        Response with 404 status code (Not Found) should be returned.
        """
        code, *_ = httpbin.request_status('')
        response_check.check_code_not_found(code)

    @pytest.allure.story('Negative')
    def test_status_invalid_code_string(self):
        """
        Handler /status/{code} should return response with same status code as was sent
        as request parameter. Valid code should be 3-digit value
        ========================================================
        Negative case with string status code value.
        Response with 400 status code (Bad Request) should be returned.
        """
        code, _, response = httpbin.request_status(get_random_string())
        response_check.check_code_bad_request(code)
        response_check.check_response_error(response)

    @pytest.allure.story('Negative')
    @pytest.mark.parametrize('status_code', [randint(1110, 9999999999), -1 * randint(1, 9999999999)],
                             ids=['unexisting code', 'negative int'])
    def test_status_invalid_code(self, status_code):
        """
        Handler /status/{code} should return response with same status code as was sent
        as request parameter. Valid code should be 3-digit value
        ========================================================
        Negative case with string status code value.
        Response with 500 status code (Server Error) should be returned.
        """
        code, *_ = httpbin.request_status(status_code)
        response_check.check_code_server_error(code)
