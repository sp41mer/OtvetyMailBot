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

