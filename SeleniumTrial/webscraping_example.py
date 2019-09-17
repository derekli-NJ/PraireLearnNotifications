from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import config

netID = config.netID
password = config.password

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path='/Users/derekli/Documents/PersonalProjects/PraireLearnNotifications/SeleniumTrial/chromedriver', chrome_options=option)
  
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

addCoursesButton = browser.find_elements_by_xpath("//*[@id='content']/div/div/a/span")[0]
addCoursesButton.click()

'''
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')
'''

"""

language_element = browser.find_elements_by_xpath("//p[@class=’mb-0 f6 text-gray’]")
# same concept as for list-comprehension above.
languages = [x.text for x in language_element]
print("languages:")
print(languages, '\n')

for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')
"""
