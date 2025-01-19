import time

import pytest

from pages.register_page import Register
from pages.conftest import browser_set_up_and_teardown


class Test_register_Page:

    @pytest.mark.usefixtures("browser_set_up_and_teardown")
    # @pytest.mark.smoke
    def test_verify_register_fun(self):
        register=Register(self.driver)
        # register.validate_register_page()
        register.login_text_validation()




