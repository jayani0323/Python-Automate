from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_results(driver):
    results = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"course-menu\"]/div/div/div[2]/div[1]/div/div/a")))
    results.click()
    print(driver.current_url)
    time.sleep(5)
    return driver

