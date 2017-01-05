# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page():

    def open(self, driver):
        driver.get(self.url)

    def wait_by_id(self,driver,id):
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except:
            print "Couldn't wait for {}".format(id)
            driver.quit()

    def wait_by_css_selector(self,driver,selector):
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        except:
            print "Couldn't wait for {}".format(selector)
            driver.quit()

    def get_by_css_selector(self,driver,selector):
        try:
            list_of_elements = driver.find_elements_by_css_selector(selector)
            if len(list_of_elements) < 2:
                return list_of_elements[0]
            else:
                return list_of_elements
        except:
            print "Couldn't find element with {}".format(selector)

