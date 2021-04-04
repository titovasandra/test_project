from gui.page_objects.BasePage import BasePage


class StartPage(BasePage):

    __email_input = {'css': '.email-input-container .email-input'}
    __enter_password_button = {'css': '[data-testid="enter-password"]'}
    __password_input = {'css': '[name="password"]'}
    __login_button = {'css': '[data-testid="login-to-mail"]'}

    def input_email(self, email):
        self._input(self.__email_input, email)

    def click_enter_password(self):
        self._click(self.__enter_password_button)

    def input_password(self, password):
        self._input(self.__password_input, password)

    def login(self):
        self._click(self.__login_button)
