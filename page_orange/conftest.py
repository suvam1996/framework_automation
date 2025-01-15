
import pytest
from page_orange.base_action import BaseAction
from page_orange.common_functions import get_value_from_input_file

global driver
# driver = None  #dought-----------



@pytest.fixture(scope="function")
def browser_set_up_and_teardown(request):
    browser = get_value_from_input_file("browser")
    web_url = get_value_from_input_file("url")
    global driver
    base_page = BaseAction(driver=None)
    driver = base_page.open_browser(browser)
    base_page.open_url(web_url)
    base_page.maximize_window_screen()
    request.cls.driver = driver
    yield
    base_page.tear_down()


