from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import config
import time
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
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/table")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()






# row = browser.find_elements_by_xpath("//*[@id='content']/div/table/tbody/tr/td/a")

def toggleCourses(toggle, browser, max_val = -1):
    #Finds body element
    body = browser.find_elements_by_xpath("/html/body/div/div/table/tbody")[0]

    #Finds the table where all entries are placed in
    entries = body.find_elements_by_tag_name("tr")
    table_size = len(entries)
    for i in range(table_size):
        entry = entries[i]
        cols = entry.find_elements_by_tag_name("td")
        #print (cols.get_attribute("outerHTML"))
        #print (cols[1 + toggle].get_attribute("outerHTML"))
        cols[1 + toggle].find_elements_by_tag_name("a")[0].click()
        
        time.sleep(0.5)

        temp = cols[1 + toggle].find_elements_by_xpath("//button[@type='submit']")[i]
        #temp = cols[1].find_elements_by_class_name("btn btn-info")[0]

        temp.click()
        
        time.sleep(0.5)
        
        body = browser.find_elements_by_xpath("/html/body/div/div/table/tbody")[0]
        entries = body.find_elements_by_tag_name("tr")
        if (i == max_val):
            break

toggleCourses(1, browser, 2)


'''
showButtons = browser.find_elements_by_xpath("//*[@id='content']/div/table/tbody/tr/td[2]/a")
buttons = browser.find_elements_by_xpath("//button[@type='submit']")
for i in range(len(showButtons)):
    showButtons = browser.find_elements_by_xpath("//*[@id='content']/div/table/tbody/tr/td[2]/a")
    buttons = browser.find_elements_by_xpath("//button[@type='submit']")
    print (buttons[i].text.lower())
    if (showButtons[0].text.lower() != "add course"):
        continue
    showButtons[0].click()
    
    #Wait for menu to load
    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
    buttons[i * 2].click()
    time.sleep(1)
'''


def saveCurrentCourses():
    enrolledCourses = open("EnrolledCourses.txt", "w")
    for entry in entries:
        nestedClass = entry.find_elements_by_class_name("modal-footer")
        for modalFooterClass in nestedClass:
            enrollForm = modalFooterClass.find_elements_by_name("enroll-form")

            if (len(enrollForm) == 0):
                #write current courses to text file
                enrolledCourses.write(entry.text + '\n')
                #print (entry.text)
    enrolledCourses.close()

def signUp(entries):
    for entry in entries:
        nestedClass = entry.find_elements_by_class_name("modal-footer")
        for modalFooterClass in nestedClass:
            enrollForm = modalFooterClass.find_elements_by_name("enroll-form")
            
            if (len(enrollForm) == 0):
                continue
            for enroll in enrollForm:
                button = enroll.find_elements_by_xpath("//button[@type='submit']")[0]
                print (button.text)

#signUp(entries)

'''
        addCourseButton = modalFooterClass.find_elements_by_class_name("btn btn-info")
        for course in addCourseButton:
            
            print (course.text)
            '''

