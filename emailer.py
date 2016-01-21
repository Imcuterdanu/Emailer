from selenium import webdriver

print(' Input your Google email address')
userEmail = input()

browser = webdriver.Firefox()
browser.get('https://mail.google.com')

logInElem = browser.find_element_by_id('Email')
logInElem.click()

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(userEmail)
emailElem.submit()

passwordElem = browser.find_element_by_id('Passwd')
userPassword = ('hello101')
passwordElem.send_keys(userPassword)

passwordElem.submit()

composeElem = browser.find_element_by_id(':3y')
composeElem.click()

userRecipent = ('haha@gmail.com')

toElem = browser.find_element_by_id(':81')
toElem.click()
toElem.send_keys(userRecipent)

subjectElem = browser.find_element_by_id(':8h')
subjectElem.click()

messageElem = browser.find_element_by_id(':8z')
messageElem.click()

sendElem = browser.find_element_by_id(':9j')
sendElem.click()