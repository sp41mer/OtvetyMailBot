# -*- coding: utf-8 -*-
import selenium
from pages.page import *

class ListLawPage(Page):

    def __init__(self):
        self.url = 'https://otvet.mail.ru/law/'
        self.page_search_class = '.page-search'
        self.question_class = '.q--li'
        self.button_show_more = '.btn.btn-more.btn-blue'
        self.question_stats_class = '.q--li--stat'
        self.stop_word = 'день'
        self.question_header_class = '.q--li--text'
        self.href_of_questions = []

    def wait_for_container(self,driver):
        self.wait_by_css_selector(driver, self.question_class)

    def scan_hrefs_of_questions(self,driver):
        self.scroll_down(driver)
        go_on = True
        while go_on:
            list_of_question_containers = self.get_by_css_selector(driver,self.question_class)
            for stat in self.get_by_css_selector(list_of_question_containers[-1],self.question_stats_class):
                if self.stop_word in stat.get_attribute('innerHTML'): go_on = False
                else: print('Go on!')
            self.scroll_down(driver)
            self.get_by_css_selector(driver,self.button_show_more).click()
            time.sleep(1)
        list_of_question_containers = self.get_by_css_selector(driver, self.question_class)
        for question in list_of_question_containers:
            link = self.get_by_css_selector(question,self.question_header_class).get_attribute('href')
            self.href_of_questions.append(link)
        return self.href_of_questions