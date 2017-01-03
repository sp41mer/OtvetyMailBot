# -*- coding: utf-8 -*-
from selenium import webdriver
from pages import *
from pages.main_page import *

driver = webdriver.Chrome('/Users/sp41mer/PycharmProjects/parcer/chromedriver')
main_page = MainPage()
main_page.open(driver=driver)
main_page.wait_for_toolbar(driver)
main_page.search(driver, u'развод')