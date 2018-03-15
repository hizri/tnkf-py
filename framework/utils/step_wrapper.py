import allure
from contextlib import contextmanager


@contextmanager
def step(description=''):
    with allure.step(description) as new_step:
        yield new_step
