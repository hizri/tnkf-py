from random import randint, choice
import string


def get_random_string():
    return ''.join([choice(string.ascii_lowercase) for _ in range(randint(3, 20))])


def get_random_headers():
    result = {}
    for _ in range(randint(1, 5)):
        key = choice([get_random_string(), '{}-{}'.format(get_random_string(), get_random_string())])
        result[key] = choice([get_random_string(), str(randint(1, 9999999))])
    return result
