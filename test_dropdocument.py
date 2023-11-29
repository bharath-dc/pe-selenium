from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestDropdocument():
    def check_for_error_and_relogin(self):
          # Wait and check if the error element appears
          try:
              WebDriverWait(self.driver, 50).until(
                  EC.presence_of_element_located((By.XPATH, '//*[@id="input-120"]'))
              )
              # If the above does not raise TimeoutException, it means the error element was found
              # Log the error, and call the login function again
              print("Login error detected, attempting to log in again.")
              self.initial_login_2()
          except Exception as e:
              # If the error element is not present, it means login was successful
              print("Logged in successfully.")

    def initial_login(self):
        self.driver.find_element(By.ID, "id_username").send_keys(
            "admin@deepcognition.ai")
        self.driver.find_element(By.ID, "id_password").send_keys("Admin@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # wait till it loads
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a'))
        )
        self.driver.find_element(
            By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a').click()

    def initial_login_2(self):
        print("dhbfaakfdblkfbdlkfbdfbldnfld")
        self.driver.find_element(By.XPATH, '//*[@id="input-120"]').send_keys(
            "admin@deepcognition.ai")
        self.driver.find_element(By.XPATH, '//*[@id="input-123"]').send_keys("Admin@1234")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # wait till it loads
       
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def fill_form(self):
        # Assuming you've navigated to the form and it's now open
        # Replace 'input_name' with the actual name or id of the form field
        self.driver.find_element(By.NAME, "shipment_id").send_keys("123456")
        # self.driver.find_element(By.NAME, "extraData").send_keys("Extra data here")
        # For dropdowns, replace 'dropdown_name' with the actual name or id
        Select(self.driver.find_element(By.NAME, "documentType")
               ).select_by_visible_text("Commercial Invoice")

        # For file upload, replace 'file_input_name' with the actual name or id
        self.driver.find_element(By.NAME, "fileInput").send_keys(
            "docs/invoice_radar_jcb.pdf")

    def verify_elements(self):
        # Replace 'element_locator' with the actual locator of the element you expect to be present
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "confirmationMessage")))
        confirmation_message = self.driver.find_element(
            By.ID, "confirmationMessage").text
        # Replace 'Success' with the actual message you're expecting
        assert "Success" in confirmation_message

    def test_dropdocument(self):
        self.driver.get("http://deepcognition4.ydns.eu:15002/#/shipments")
        self.initial_login()
        self.check_for_error_and_relogin()
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div[1]/main/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/table/thead/tr/th[8]/div[1]/span[1]'))
            )
        
        except Exception as e:
            print("Page did not load after login.")
       
        self.fill_form()
      
        self.driver.find_element(
            By.CSS_SELECTOR, "submit_button_selector").click()
        # self.verify_elements()
