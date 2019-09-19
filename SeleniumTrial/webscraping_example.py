from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import config
import os, sys

netID = config.netID
password = config.password

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

#browser = webdriver.Chrome(executable_path='/Users/derekli/Documents/PersonalProjects/PraireLearnNotifications/SeleniumTrial/chromedriver', chrome_options=option)
os.path.join(sys.path[0], 'some file.txt')
browser = webdriver.Chrome(executable_path=os.path.join(sys.path[0], 'chromedriver'), chrome_options=option)


browser.get("https://prairielearn.engr.illinois.edu/pl/login")


# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div/a[1]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# Find Illinois login button
illinoisLoginButton = browser.find_elements_by_xpath("/html/body/div/div/div/div/a[1]")[0]
illinoisLoginButton.click()

#Wait for login form to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/form/div[1]/input")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

usernameField = browser.find_elements_by_xpath("/html/body/main/form/div[1]/input")[0]
usernameField.send_keys(netID)

passwordField = browser.find_elements_by_xpath("/html/body/main/form/div[2]/input")[0]
passwordField.send_keys(password)

loginButton = browser.find_elements_by_xpath("/html/body/main/form/div[3]/input")[0]
loginButton.click()


#Wait for add courses button to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div/div/a/span")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

addCoursesPageButton = browser.find_elements_by_xpath("//*[@id='content']/div/div/a/span")[0]
addCoursesPageButton.click()


#Wait for courses to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/table/tbody/tr[1]/td[2]/a")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


body = browser.find_elements_by_xpath("/html/body/div/div/table/tbody")[0]

entries = body.find_elements_by_tag_name("tr")

for entry in entries:
    courses = entry.find_elements_by_class_name("align-middle")
    for course in courses:
        print (course.text)

