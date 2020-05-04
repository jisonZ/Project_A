from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up your chromedriver location
# --------------------------------
DRIVER_PATH = "C:\\Users\\...\\chromedriver.exe"
# --------------------------------
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

wd.get('http://www.gmail.com')
elem = wd.find_element_by_id('identifierId')
# Set up your email address here
# ------------------------------
My_email = 'myemail@umich.edu'
# ------------------------------
elem.send_keys(My_email + Keys.RETURN)

#UM login
login = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.ID, 'login')))
password = wd.find_element_by_id('password')
# Set up login unique_name and password
# -------------------------------------
login.send_keys('Uniquename')
password.send_keys('password' + Keys.RETURN)
# -------------------------------------

#DUO login
wd.switch_to.frame(0)
send_push = wd.find_element_by_css_selector(".push-label > .auth-button").click()
wd.switch_to.default_content()
approve = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , ".zZhnYe .RveJvd")))
approve.click()

#Write Email
New_mail = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , ".T-I-KE")))
New_mail.click()
address = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME , "to")))
# Set up the email address you want to send to
# --------------------------------------------
address.send_keys('someone@umich.edu')
# --------------------------------------------
title = wd.find_element_by_name('subjectbox')
# Set up subject title
# -------------------
title.send_keys('This is a sample title')
# -------------------
content = wd.find_elements_by_xpath('//td[2]/div[2]/div')
# Set up content
# --------------
content[0].send_keys('this is a sample mail')
# --------------
send = wd.find_elements_by_xpath('//div[4]/table/tbody/tr/td/div/div[2]/div')
send[0].click()

time.sleep(10)
wd.quit()