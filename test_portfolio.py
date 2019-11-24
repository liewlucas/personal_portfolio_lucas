import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#launch site (index page)
def test_launchportfoliosite():
    driver = webdriver.Chrome()
    result = driver.get("localhost:8000/projects")
    assert result == driver.get("localhost:8000/projects")

#input wrong link and failed to launch site
def test_launchportfoliositefail():
    driver = webdriver.Chrome()
    result = driver.get("localhost:8000/projectss")
    assert result == driver.get("localhost:8000/projectss")


#testing read more button on projects
def test_readmore_button():
    driver = webdriver.Chrome()
    driver.get('localhost:8000/projects')
    element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/a").click()
    assert element == driver.get('localhost:8000/projects/1')
    driver.quit()
    
#admin login rightful credentials
def test_admin_login():
    driver = webdriver.Chrome()
    driver.get("localhost:8000/admin")
    Username = "liewlucas"
    Password = "llll8888"

    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password"]')

    user.send_keys(Username)
    com.send_keys(Password)

    login = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    assert login == driver.get('localhost:8000/admin')#login to admin page 
    driver.quit()

#admin login wrong credentials
def test_admin_logininvalid():
    driver = webdriver.Chrome()
    driver.get("localhost:8000/admin")
    Username = "admin123"
    Password = "121345"

    user = driver.find_element_by_xpath('//*[@id="id_username"]')
    com = driver.find_element_by_xpath('//*[@id="id_password"]')

    user.send_keys(Username)
    com.send_keys(Password)

    login = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    assert login == driver.get('localhost:8000/admin') 
    driver.quit()



#test commenting on blog
def test_comment_blog():
    driver = webdriver.Chrome()
    driver.get("localhost:8000/blog/2")

    cmtname = 'King'
    cmtdesc = 'This is nothing compared to what i do'

    name = driver.find_element_by_xpath('//*[@id="id_author"]')
    comment = driver.find_element_by_xpath('//*[@id="id_body"]')

    name.send_keys(cmtname)
    comment.send_keys(cmtdesc)

    submitcmt = driver.find_element_by_xpath('/html/body/div/div/form/button').click()
    assert submitcmt == driver.get('localhost:8000/blog/2') #page reloads upon submitting comment
    driver.quit()



#test commenting on blog with empty fields
def test_comment_blog_empty():
    driver = webdriver.Chrome()
    driver.get("localhost:8000/blog/2")

    cmtname = ''
    cmtdesc = ''

    name = driver.find_element_by_xpath('//*[@id="id_author"]')
    comment = driver.find_element_by_xpath('//*[@id="id_body"]')

    name.send_keys(cmtname)
    comment.send_keys(cmtdesc)

    submitcmt = driver.find_element_by_xpath('/html/body/div/div/form/button').click()
    assert submitcmt == driver.get('localhost:8000/blog/2') #page reloads upon submitting comment
    driver.quit()
