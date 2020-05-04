# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestYoutubesearch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_youtubesearch(self):
    # Test name: Youtube_search
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.youtube.com/")
    # 2 | setWindowSize | 1740x941 | 
    self.driver.set_window_size(1740, 941)
    # 3 | click | name=search_query | 
    self.driver.find_element(By.NAME, "search_query").click()
    # 4 | type | name=search_query | this is america
    self.driver.find_element(By.NAME, "search_query").send_keys("this is america")
    # 5 | sendKeys | name=search_query | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "search_query").send_keys(Keys.ENTER)
    # 6 | mouseOver | css=.ytd-item-section-renderer:nth-child(1) > #dismissable #video-title > .style-scope | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ytd-item-section-renderer:nth-child(1) > #dismissable #video-title > .style-scope")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | click | css=.ytd-item-section-renderer:nth-child(1) > #dismissable #video-title > .style-scope | 
    self.driver.find_element(By.CSS_SELECTOR, ".ytd-item-section-renderer:nth-child(1) > #dismissable #video-title > .style-scope").click()
    # 8 | mouseOut | css=.ytd-item-section-renderer:nth-child(1) > #dismissable #video-title > .style-scope | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 9 | mouseOver | css=.ytp-play-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | click | css=.ytp-play-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".ytp-play-button").click()
    # 11 | mouseOut | css=.ytp-play-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 12 | mouseOver | css=.ytd-compact-radio-renderer > #thumbnail #img | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ytd-compact-radio-renderer > #thumbnail #img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | css=.ytd-compact-radio-renderer > #thumbnail #img | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 14 | mouseOver | css=#hover-overlays > .style-scope | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#hover-overlays > .style-scope")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | close |  | 
    self.driver.close()
  
