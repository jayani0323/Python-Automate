from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.append("C:\\Users\\Jayani\\Desktop\\Assignment-elearning")
from selenium.webdriver.common.by import By
from pages.Home.home_page import search_python_course
from pages.Results.results_page import check_results
from pages.Courses.course_page import check_course_content, generate_report

# Create a Properties 
properties = Properties()

# Load properties from file
with open('testcase.properties', 'rb') as f:
    properties.load(f, 'utf-8')

# Access values
test_url = properties.get('test_url')[0]
print(test_url)

def google_search():
    service = webdriver.ChromeService(executable_path = 'C:\\Users\\Jayani\\Desktop\\Assignment-elearning\\driver\\chromedriver.exe') 
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(test_url)
    search_bar = driver.find_element(By.XPATH, "//*[@id=\"APjFqb\"]")
    search_bar.send_keys("eLearning.lk")
    search_bar.send_keys(Keys.RETURN)
    first_result = driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
    first_result.click()
    print(driver.current_url)

    driver = search_python_course(driver)
    driver = check_results(driver)
    
    return driver

def check_course():
    driver = google_search()
    driver = check_course_content(driver)
    driver = generate_report(driver)
    driver.close()
   
check_course()