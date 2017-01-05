# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from pages import *
from pages.main_page import *
from pages.list_page import *
from pages.answer_page import *

url_modificators = {
    'categories': {
        'administrative': '/c-1454',
        'army': '/c-1464',
        'civil': '/c-1455',
        'house': '/c-1461',
        'constitution': '/c-1456',
        'passport': '/c-1465',
        'social': '/c-1462',
        'family': '/c-1457',
        'work': '/c-1458',
        'crime': '/c-1459',
        'financial': '/c-1460',
        'other': '/c-1466'
    },
    'dates': {
        'today': '/p-86400',
        'three_days': '/p-259200',
        'week': '/p-604800',
        'month': '/p-2592000',
        'year': '/p-31536000',
        'forever': None
    },
    'types': {
        'questions_and_answers': None,
        'only_questions': '/w-q',
        'only_answers': '/w-a'
    }
}

driver = webdriver.Chrome('/Users/sp41mer/PycharmProjects/parcer/chromedriver')
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
    print title
    print content

