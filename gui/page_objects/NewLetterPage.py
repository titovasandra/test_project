from gui.page_objects.BasePage import BasePage


class NewLetterPage(BasePage):

    __addressee_field = {'css': '[tabindex="100"]'}
    __content_letter_field = {'css': '[tabindex="505"]'}
    __send_button = {'css': '[tabindex="570"]'}

    def input_addressee(self, addressee_email):
        self._input(self.__addressee_field, addressee_email)

    def enter_text_letter(self, text):
        self._input(self.__content_letter_field, text)

    def send_letter(self):
        self._click(self.__send_button)
