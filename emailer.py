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

subjectElem = browser.find_element_by_id(':8i')
subjectElem.click()

subjectElem.send_keys(subject)
subject = ('subject')

messageElem = browser.find_element_by_id(':9o')
messageElem.click()

subjectElem.send_keys(message)
message = ('PYTHON IS SO ANNOYING')