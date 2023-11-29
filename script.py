from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # Import Service
from selenium.webdriver.common.by import By
import csv

# Initialize WebDriver
gecko_driver_path = "geckodriver.exe"  # Replace with the path to your GeckoDriver
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
# URLs
driver.get('http://deepcognition10.ydns.eu:12622')
username = "admin@deepcognition.ai"
password = "Admin@1234"

def initial_login():
    try:
        # Your test code here
        username_field = driver.find_element(By.NAME, "username")  # Updated method
        password_field = driver.find_element(By.NAME, "password")  # Updated method
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Find and click the login button
        login_button = driver.find_element(By.XPATH, "/html/body/div/div/form/div[1]/div[3]/button")  # Updated method
        login_button.click()
        result = "Pass"
        remark = ""
    except Exception as e:
        result = "Fail"
        remark = str(e)
    return initial_login.__name__, result, remark

def drop_doc():
    #drops document
def validator_test():
    #checks functions in validator
# Writing results to a report
with open('test_report.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Function Tested', 'Result', 'Remarks'])
    function_name, result, remark = initial_login()
    writer.writerow([function_name, result, remark])

# Close the browser
driver.quit()
