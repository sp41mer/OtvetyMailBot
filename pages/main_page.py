# -*- coding: utf-8 -*-
import selenium
import time
from pages.page import *
from pages.list_page import *

class MainPage(Page):

    def __init__(self):
        self.url = "https://otvet.mail.ru"
        self.toolbar_id = 'portal-menu__toolbar'
        self.search_bar_input_class = '.js-input.pm-toolbar__search__input.pm-toolbar__search__input_not-expandable.pm-toolbar__search__input_not-adaptive'
        self.search_bar_button_class = '.js-submit-button.pm-toolbar__search__button__input.pm-toolbar__search__button__input_not-expandable.pm-toolbar__search__button__input_not-adaptive'
        self.enter_button_id = '#PH_authLink'
        self.login_panel_class = '.b-panel.b-panel_service.b-panel_login.b-panel_fullscreen'
        self.login_panel__login_class = '.b-input.b-input_in-row.b-input_b-login-providers.b-input_.b-input_popup'
        self.login_panel__password_class = '.b-input.b-input_in-row.b-input_password.b-input_.b-input_popup'
        self.login_panel__submit_class = 'btn.btn_stylish.btn_main.btn_single.btn_fluid.btn_form btn_.b-login__submit-btn'

    def wait_for_toolbar(self,driver):
        self.wait_by_id(driver, self.toolbar_id)

    def wait_for_login(self,driver):
        self.wait_by_css_selector(driver, self.login_panel__login_class)

    def search(self,driver, query):
        bar = driver.find_element_by_css_selector(self.search_bar_input_class)
        bar.send_keys(query)
        bar_button = driver.find_element_by_css_selector(self.search_bar_button_class)
        bar_button.click()
        next_page = ListPage(driver)
        next_page.wait_for_container(driver)

    def login(self, driver, login, password):
        #TODO: Починить это дерьмо !
        button = driver.find_element_by_css_selector(self.enter_button_id)
        button.click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_css_selector('.ag-popup__frame__layout__iframe'))
        self.wait_for_login(driver)
        login_input = driver.find_element_by_css_selector(self.login_panel__login_class)
        password_input = driver.find_element_by_css_selector(self.login_panel__password_class)
        login_input.send_keys(login)
        password_input.send_keys(password)
        submit_buttons = driver.find_element_by_css_selector(self.login_panel__submit_class)
        submit_buttons.click()
        driver.switch_to_default_content()
        time.sleep(2)
        self.open(driver)










