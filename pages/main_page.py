# -*- coding: utf-8 -*-
import selenium
from page import *

class MainPage(Page):

    def __init__(self):
        self.url = "https://otvet.mail.ru"
        self.toolbar_id = 'portal-menu__toolbar'
        self.search_bar_input_class = '.js-input.pm-toolbar__search__input.pm-toolbar__search__input_not-expandable.pm-toolbar__search__input_not-adaptive'
        self.search_bar_button_class = '.js-submit-button.pm-toolbar__search__button__input.pm-toolbar__search__button__input_not-expandable.pm-toolbar__search__button__input_not-adaptive'

    def wait_for_toolbar(self,driver):
        self.wait_by_id(driver, self.toolbar_id)

    def search(self,driver, query):
        bar = driver.find_element_by_css_selector(self.search_bar_input_class)
        bar.send_keys(query)
        bar_button = driver.find_element_by_css_selector(self.search_bar_button_class)
        bar_button.click()

