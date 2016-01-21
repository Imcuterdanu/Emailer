from selenium import webdriver

print(' Input your Google email address')
userEmail = ('littlejustin12345@gmail.com')

browser = webdriver.Firefox()
browser.get('https://mail.google.com')

logInElem = browser.find_element_by_id('Email')
logInElem.click()

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(userEmail)
emailElem.submit()

print(' Input your Google email password')
Pass = input()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(Pass)
passwordElem.submit()

composeElem = browser.find_element_by_id(':3y')
composeElem.click()

userRecipent = ('haha@gmail.com')

toElem = browser.find_element_by_id(':8w')
toElem.click()
toElem.send_keys(userRecipent)

subjectElem = browser.find_element_by_id(':8h')
subjectElem.click()

messageElem = browser.find_element_by_id(':9j')
messageElem.click()

sendElem = browser.find_element_by_id(':87')
sendElem.click()