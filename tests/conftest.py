import pytest
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

from framework.utils.logger import buffer_stream


@pytest.fixture(scope='function', autouse=True)
def attach_full_log(request):
    # Attaches full buffered log on every test teardown
    def attach_and_clear_buffer():
        attach(buffer_stream.getvalue(), 'Full log', attachment_type=AttachmentType.TEXT)
        buffer_stream.truncate(0)
        buffer_stream.seek(0)
    request.addfinalizer(attach_and_clear_buffer)
