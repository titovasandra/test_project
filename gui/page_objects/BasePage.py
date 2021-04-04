from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __get_element(self, selector):
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_element(by, selector)

    def _click(self, selector):
        self.__get_element(selector).click()

    def _input(self, selector, value):
        self.__get_element(selector).send_keys(value)

