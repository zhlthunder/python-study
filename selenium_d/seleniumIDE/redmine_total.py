# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RedmineTotal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.hostedredmine.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_redmine_total(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("zhuerma")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("zhl040702246")
        driver.find_element_by_id("login-submit").click()
        driver.find_element_by_css_selector("span.drdn-trigger").click()
        driver.find_element_by_link_text("zhl").click()
        driver.find_element_by_link_text(u"问题").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'新建问题')])[3]").click()
        driver.find_element_by_id("issue_subject").clear()
        driver.find_element_by_id("issue_subject").send_keys("ppppp")
        driver.find_element_by_id("issue_description").clear()
        driver.find_element_by_id("issue_description").send_keys("aaaaaaaaaaaaa")
        Select(driver.find_element_by_id("issue_priority_id")).select_by_visible_text("High")
        Select(driver.find_element_by_id("issue_assigned_to_id")).select_by_visible_text(u"<< 我 >>")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"编辑").click()
        Select(driver.find_element_by_id("issue_done_ratio")).select_by_visible_text("100 %")
        driver.find_element_by_id("issue_notes").clear()
        driver.find_element_by_id("issue_notes").send_keys("close")
        driver.find_element_by_css_selector("#issue-form > input[name=\"commit\"]").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"您确定要删除选中的问题吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"退出").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
