from framework.data.constants import BASE_URL, HEADERS, REDIRECT, STATUS
from framework.utils.service_utils import send_request


def request_headers(headers=None):
    url = '{}{}'.format(BASE_URL, HEADERS)
    return send_request(url, headers=headers)


def request_redirect(count):
    url = '{}{}{}'.format(BASE_URL, REDIRECT, count)
    return send_request(url, return_history=True)


def request_status(status):
    url = '{}{}{}'.format(BASE_URL, STATUS, status)
    return send_request(url)
