from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_course_content(driver):
    course_content = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[3]/div/div/div/div[2]")))
    print(course_content.text)
    print(driver.current_url)
    
    time.sleep(5)
    return driver

def generate_report(driver):
    print("Generating report...")
    report_file_path = "course_content_report.txt"
    course_content = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[3]/div/div/div/div[2]")))
    with open(report_file_path, "w", encoding="utf-8") as file:
        file.write(course_content.text)

    # print(f"Report generated at: {os.path.abspath(report_file_path)}")
    
    time.sleep(5)
    return driver




  

    