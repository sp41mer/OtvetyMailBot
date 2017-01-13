# -*- coding: utf-8 -*-
from pages.main_page import *
from pages.list_page import *
from pages.answer_page import *
from models.bot_models import Question
from utils import url_modificators, driver_place
from nlp import make_word_vector
from selenium import webdriver
import re
import datetime

driver = webdriver.Chrome(driver_place)
main_page = MainPage()
main_page.open(driver=driver)
main_page.wait_for_toolbar(driver)
main_page.search(driver, u'развод')
url = driver.current_url
modificator = url_modificators['categories']['family']+\
              url_modificators['dates']['three_days']+\
              url_modificators['types']['only_questions']
url = re.sub(r'(\bsearch\b)', r'\1{}'.format(modificator), url)
driver.get(url)
list_page = ListPage(driver)
list_page.open(driver)
list_page.wait_for_container(driver)
list_page.scan_hrefs_of_questions(driver)
for href in list_page.href_of_questions:
    question = AnswerPage(href)
    question.open(driver)
    question.wait_for_question(driver)
    title = question.get_question_title(driver)
    content = question.get_question_comment(driver)
    inf_title = make_word_vector(title)
    if content:
        inf_content = make_word_vector(content)
    try:
        Question.create(
            date=datetime.datetime.now(),
            href=href,
            title=title,
            content=content,
            inf_title=inf_title,
            inf_content=inf_content
        )
    except Exception as e:
        print e
        print 'Not unique url!'

