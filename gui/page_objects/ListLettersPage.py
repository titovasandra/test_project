from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gui.page_objects.BasePage import BasePage


class ListLettersPage(BasePage):

    __new_letter_button = {'css': '.compose-button'}

    def create_new_letter(self):
        self._wait_for_presence(self.__new_letter_button)
        self._click(self.__new_letter_button)

    def _wait_for_presence(self, selector):
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
