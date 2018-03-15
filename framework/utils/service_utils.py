import json

import requests
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

from framework.data.constants import BASE_URL, HEADERS, STATUS, REDIRECT
from framework.utils.logger import logger
from framework.utils.step_wrapper import step


def send_request(url, method='GET', headers=None, timeout=None, allow_redirects=True, verify=True,
                 return_history=False):
    if headers is None:
        headers = {}
    with step('Sending request to URL "{}"'.format(url)):
        logger.info('Sending request to URL: "{}"\n'.format(url))
        _log_add_separator()
        try:
            response = requests.request(url=url, method=method, headers=headers, timeout=timeout,
                                        allow_redirects=allow_redirects, verify=verify)
        except (ConnectionError, TimeoutError) as e:
            _log_exception(e)
            raise
    if json_response(response):
        response_content = response.json()
    else:
        response_content = response.text

    # log request
    _log_request(url, response)

    # curl into log
    _log_curl(url, response)

    # response into log
    _log_response(response)
    if return_history:
        return response.status_code, response.headers, response.history, response_content
    return response.status_code, response.headers, response_content


def json_response(response):
    return 'application/json' in response.headers.get('Content-Type', [])


def _request_as_curl(url, response):
    _curl = 'curl {method} {headers} {data} "{url}"'
    headers = response.request.headers
    curl_headers = ''
    if headers:
        s = ['"{}:{}"'.format(k, v) for k, v in headers.items()]
        curl_headers = '-H ' + ' -H '.join(s)
    curl_data = '' if response.request.body is None else "-d '{%s}'" % response.request.body
    return _curl.format(method='-X {}'.format(response.request.method),
                        headers=curl_headers,
                        data=curl_data,
                        url=url)


def _log_curl(url, response):
    logger.info('As CURL: {}'.format(_request_as_curl(url, response)))
    _log_add_separator()


def _log_request(url, response):
    headers = json.dumps(dict(response.request.headers), indent=4, sort_keys=True)
    request_body = '' if not response.request.body else response.request.body
    logger.info('URL: {}\n'
                'Headers:\n{}\n'
                'Request body:\n{}'.format(url, headers, request_body))
    _log_add_separator()


def _log_response(response):
    is_json_response = json_response(response)
    headers = json.dumps(dict(response.headers), indent=4, sort_keys=True)
    response_body = response.json() if is_json_response else response.text
    with step('Received response'):
        logger.info('Received response:')
        logger.info('Headers:\n%s\n'
                    'Code: %s\n'
                    'Response body:\n%s' % (headers, response.status_code, json.dumps(response_body, indent=4)))
        attach(headers, 'Response headers', attachment_type=AttachmentType.TEXT)
        if is_json_response:
            attach(json.dumps(response_body, indent=4, sort_keys=True), 'Response body',
                   attachment_type=AttachmentType.JSON)
        else:
            attach(response_body, 'Response body', attachment_type=AttachmentType.HTML)
        _log_add_separator()


def _log_exception(exception):
    logger.exception('Exception was handled! Details\n{}'.format(exception))


def _log_add_separator():
    logger.info('=' * 68)
