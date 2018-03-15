from contextlib import contextmanager

import allure


@contextmanager
def step(description=''):
    with allure.step(description) as new_step:
        yield new_step
