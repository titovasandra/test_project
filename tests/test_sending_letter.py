from gui.page_objects.ListLettersPage import ListLettersPage
from gui.page_objects.NewLetterPage import NewLetterPage
from gui.page_objects.StartPage import StartPage


def test_sending_letter(browser):
    start_page = StartPage(browser)
    start_page.input_email('test-email@mail.ru')
    start_page.click_enter_password()
    start_page.input_password('test-password')
    start_page.login()
    ListLettersPage(browser).create_new_letter()
    new_letter_page = NewLetterPage(browser)
    new_letter_page.input_addressee('test-email@mail.ru')
    new_letter_page.enter_text_letter('Letter text')
    new_letter_page.send_letter()
