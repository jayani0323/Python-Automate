from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.append("C:\\Users\\Jayani\\Desktop\\Assignment-elearning")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from behave import *

@given('we go to elearning.lk site')
def google_search(context):
    context.service = webdriver.ChromeService(executable_path = 'C:\\Users\\Jayani\\Desktop\\Assignment-elearning\\driver\\chromedriver.exe') 
    context.driver = webdriver.Chrome(service=context.service)
    context.driver.maximize_window()
    context.driver.get('https://www.google.com/')
    search_bar = context.driver.find_element(By.XPATH, "//*[@id=\"APjFqb\"]")
    search_bar.send_keys("eLearning.lk")
    search_bar.send_keys(Keys.RETURN)
    first_result = context.driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
    first_result.click()
    print(context.driver.current_url)
    # return driver

@when('we search for "{search_text}" in serach bar and click search')
def search_python_course(context, search_text):
    # search_text = "Python Course"
    search= WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[1]/div/div/div/div[2]/form/input")))
    search.send_keys(search_text)
    search.send_keys(Keys.RETURN) 
    
    

@then('we should redirect to the python course results page')
def check_results(context):
    results = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"course-menu\"]/div/div/div[2]/div[1]/div/div/a")))
    results.click()
    print(context.driver.current_url)
  

# def check_course_content(context):
#     course_content = WebDriverWait(context.driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[3]/div/div/div/div[2]")))
#     print(course_content.text)
#     print(context.driver.current_url)   

