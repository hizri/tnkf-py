import jsonschema
import requests
from hamcrest import assert_that, equal_to

from framework.utils.step_wrapper import step


@step('Check that response code is 200')
def check_status_code_ok(status_code):
    assert_that(status_code, equal_to(requests.codes.ok))


@step('Check that response code is 400')
def check_code_bad_request(status_code):
    assert_that(status_code, equal_to(requests.codes.bad_request))


@step('Check that response code is 404')
def check_code_not_found(status_code):
    assert_that(status_code, equal_to(requests.codes.not_found))


@step('Check that response code is 500')
def check_code_server_error(status_code):
    assert_that(status_code, equal_to(requests.codes.internal_server_error))


@step('Check that response code matches expected one')
def check_status_code_matches_expected(response_code, expected_code):
    assert_that(response_code, equal_to(expected_code), f"""Expected code doesn't match expected\n
                                                            Response code: {response_code}\n
                                                            Expected: {expected_code}\n""")


@step('Check that response is "Invalid status code"')
def check_response_error(response):
    assert_that(response, equal_to('Invalid status code'))


@step('Check redirect count')
def check_redirect_count(response_history, expected_count):
    assert_that(len(response_history), equal_to(expected_count))
    for item in response_history:
        assert_that(item.status_code, equal_to(302))


@step('Validate json schema')
def validate_json_schema(response, schema):
    jsonschema.validate(response, schema)
