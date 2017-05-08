# -*- coding: utf-8 -*-
import selenium
from pages.page import *
from antigate import AntiGate
from PIL import Image

class AnswerPage(Page):

    def __init__(self, url):
        self.url = url
        self.title = ''
        self.content = ''
        self.question_header_class = '.q--qtext.entry-title'
        self.question_comment_class = '.q--qcomment.h4.entry-content'
        self.question_answer__input_class = '.form--text'
        self.question_answer__source_class = '.form--source'
        self.question_answer__submit_class = '.btn.btn-orange.action--save'
        self.question_get_answer = '.btn.btn-orange.action--scroll-to-reply.action--need-auth'
        self.agreement = '.h5.gray.agreement'
        self.capcha_popup = '.popup--content'

    def wait_for_question(self, driver):
        self.wait_by_css_selector(driver, self.question_header_class)

    def wait_for_capcha(self,driver):
        self.wait_by_css_selector(driver, self.capcha_popup)

    def get_question_title(self, driver):
        self.title = self.get_by_css_selector(driver, self.question_header_class).text
        return self.title

    def get_question_comment(self, driver):
        if self.get_by_css_selector(driver, self.question_comment_class):
            self.content = self.get_by_css_selector(driver, self.question_comment_class).text
        return self.content

    def make_answer(self,driver,answer,source):
        scroll_answer = self.get_by_css_selector(driver,self.question_get_answer)
        input_answer = self.get_by_css_selector(driver,self.question_answer__input_class)
        input_source = self.get_by_css_selector(driver,self.question_answer__source_class)
        input_submit = self.get_by_css_selector(driver,self.question_answer__submit_class)
        try:
            scroll_answer.click()
            # input_submit.location_once_scrolled_into_view
            input_answer.send_keys(answer)
            input_source.send_keys('http://eshche.ru')
            input_submit.click()
            try:
                self.wait_for_capcha(driver)
                capcha = self.get_by_css_selector(driver, self.capcha_popup)
                image_capcha = self.get_by_css_selector(capcha, 'img')
                driver.save_screenshot('screenshot.png')
                im = Image.open('screenshot.png')
                left = int(image_capcha.location_once_scrolled_into_view['x'] * 2)
                top = int(image_capcha.location_once_scrolled_into_view['y'] * 2)
                right = left + image_capcha.size['width'] * 2
                bottom = top + image_capcha.size['height'] * 2
                im = im.crop((left, top, right, bottom))
                im.save('screenshot.jpg')
                capcha = AntiGate('Place your password', 'screenshot.jpg')
                print(capcha)
            except:
                pass
            return True
        except:
            return False


    def scroll_to_element(self,element):
        pass