# -*- coding: utf-8 -*-
from pages.main_page import *
from pages.list_page import *
from pages.answer_page import *
from pages.list_law_page import *
from models.bot_models import Question
from utils import url_modificators, driver_place
from nlp import make_word_vector
from selenium import webdriver
import re
import datetime
import time


def search_for_keyword(keyword):
    driver = webdriver.Chrome(driver_place)
    main_page = MainPage()
    main_page.open(driver=driver)
    main_page.wait_for_toolbar(driver)
    main_page.search(driver, keyword)
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
        else:
            inf_content = ''
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
            print(e)
            print('Not unique url!')

def scan_one_day_questions():
    logined_driver = login()
    list_law_page = ListLawPage()
    list_law_page.open(logined_driver)
    list_law_page.wait_for_container(logined_driver)
    hrefs = list_law_page.scan_hrefs_of_questions(logined_driver)
    for href in hrefs:
        question = AnswerPage(href)
        question.open(logined_driver)
        question.wait_for_question(logined_driver)
        title = question.get_question_title(logined_driver)
        content = question.get_question_comment(logined_driver)
        inf_title = make_word_vector(title)
        if content:
            inf_content = make_word_vector(content)
        else:
            inf_content = ''
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
            print(e)
            print('Not unique url!')

def give_answers():
    for question in Question.select().where(Question.isAnswered==0):
        if question.answer:
            answer = question.answer
            logined_driver = login()
            answer_page = AnswerPage(question.href)
            answer_page.open(logined_driver)
            answer_page.wait_for_question(logined_driver)
            if answer_page.make_answer(logined_driver,answer,source='http://eshche.ru'):
                question.isAnswered = 1
                question.save()
                time.sleep(60)
            logined_driver.quit()

def login():
    driver = webdriver.Chrome(driver_place)
    driver.get('https://mail.ru/')
    driver.find_element_by_css_selector('#mailbox__login').send_keys('stepanov_lawyer')
    # driver.find_element_by_css_selector('#mailbox__password').send_keys('Elo7&V2xHBtc')
    driver.find_element_by_css_selector('#mailbox__auth__button').click()
    time.sleep(3)
    return driver


# scan_one_day_questions()
# give_answers()


