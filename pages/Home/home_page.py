from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
sys.path.append("C:\\Users\\Jayani\\Desktop\\Assignment-elearning")

def search_python_course(driver):
    search_text = "Python Course"
    # search = driver.find_element(By.XPATH, "//*[@id=\"searching-text\"]")
    search= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[1]/div/div/div/div[2]/form/input")))
  

    search.send_keys(search_text)
    search.send_keys(Keys.RETURN) 
    print(driver.current_url)
    # print(driver.current_url)
    # result = WebDriverWait(driver, 40).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[@id=\"course-menu\"]/div/div/div[2]/div[1]/div/div/a")))
    # result.click()
    time.sleep(5)

    return driver
