import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestVali:
    def setup_method(self):
        # Setup method to initialize the webdriver before each test
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        # Teardown method to close the webdriver after each test
        self.driver.quit()

    def initial_login(self):
        # Method for initial login
        self.driver.get("http://deepcognition4.ydns.eu:15002")
        self.driver.find_element(By.ID, "id_username").send_keys("admin@deepcognition.ai")
        self.driver.find_element(By.ID, "id_password").send_keys("Admin@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a'))
        # )
        # self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a').click()

    def test_validate(self):
        # Main test method
        self.driver.get("http://deepcognition4.ydns.eu:15002")
        self.initial_login()
        # Navigate to a specific page
        self.driver.get("http://deepcognition4.ydns.eu:15002/validate?task_id=1701409514688")
        self.driver.set_window_size(1589, 834)

        # Interacting with various elements on the page
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle:nth-child(2)").click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.sliderWrapper:nth-child(1) .slider'))
        )
        self.driver.find_element(By.CSS_SELECTOR, ".sliderWrapper:nth-child(1) .slider").click()
        self.driver.find_element(By.ID, "runcheck-btn1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sliderWrapper:nth-child(2) .slider").click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sliderWrapper:nth-child(3) .slider"))
        )
        self.driver.find_element(By.CSS_SELECTOR, ".sliderWrapper:nth-child(3) .slider").click()
        self.driver.find_element(By.ID, "runcheck-btn1").click()
        self.driver.find_element(By.CSS_SELECTOR, "#check_status_text > .badge").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsPanel-btn-close > .jsPanel-icon").click()
        self.driver.find_element(By.CSS_SELECTOR, "#check_status_text > .badge").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsPanel-btn-close > .jsPanel-icon").click()
        self.driver.find_element(By.CSS_SELECTOR, "#publish_status_text > .badge").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jsPanel-btn-close path").click()
        self.driver.find_element(By.ID, "line-item-btn").click()
        self.driver.find_element(By.ID, "line-item-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nav").click()
        self.driver.find_element(By.ID, "btnGroupDrop1").click()
        self.driver.find_element(By.ID, "btnGroupDrop1").click()
        self.driver.find_element(By.ID, "btnGroupDrop1").click()
        self.driver.find_element(By.ID, "export-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".svgclass > svg").click()

# Note: This script assumes that the elements being interacted with are present and accessible on the page. 
# If elements are dynamically loaded or if there are timing issues, you may need to add appropriate waits or checks.
