# -*- coding: utf-8 -*-
import selenium
from page import *

class AnswerPage(Page):

    def __init__(self, url):
        self.url = url
        self.title = ''
        self.content = ''
        self.question_header_class = '.q--qtext.entry-title'
        self.question_comment_class = '.q--qcomment.h4.entry-content'

    def wait_for_question(self, driver):
        self.wait_by_css_selector(driver, self.question_header_class)

    def get_question_title(self, driver):
        self.title = self.get_by_css_selector(driver, self.question_header_class).text
        return self.title

    def get_question_comment(self, driver):
        if self.get_by_css_selector(driver, self.question_comment_class):
            self.content = self.get_by_css_selector(driver, self.question_comment_class).text
        return self.content