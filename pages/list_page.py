# -*- coding: utf-8 -*-
import selenium
from page import *

class ListPage(Page):

    def __init__(self, driver):
        self.url = driver.current_url
        self.page_search_class = '.page-search'
        self.question_container_class = '.gray-line.dotted.item.item_ava.item_similiar'
        self.question_header_class = '.blue.item__text'
        self.href_of_questions = []

    def wait_for_container(self,driver):
        self.wait_by_css_selector(driver, self.page_search_class)

    def scan_hrefs_of_questions(self,driver):
        list_of_question_containers = self.get_by_css_selector(driver,self.question_container_class)
        for question in list_of_question_containers:
            link = self.get_by_css_selector(question,self.question_header_class).get_attribute('href')
            self.href_of_questions.append(link)



