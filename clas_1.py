from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment to run without opening browser
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)
# options.experimental_options("detach",True)
#
# # ✅ Use Service() with path to chromedriver
myService = Service("/Users/apple/Documents/chromedriver/142.0.7444.176_chromedriver-mac-x64/chromedriver")
driver = webdriver.Chrome(service=myService, options=options)
driver.maximize_window()

def test_open_element_page():
    driver.get("https://demoqa.com/automation-practice-form")
    driver.implicitly_wait(9)

    first_element = driver.find_element(By.ID, "firstName")
    first_element.send_keys("Testing")

    second_element = driver.find_element(By.XPATH, "//input[@id='lastName']")
    second_element.send_keys("selenium")


    # gender_element = driver.find_element(By.XPATH, '//input[@id="gender-radio-2"]')
    # gender_element.click()

    hobby1_element = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobby1_element.click()
    #
    # hobby2_element = driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-3"]')
    # hobby2_element.click()

def test_local_element_page():
    driver.get("file:/Users/apple/Documents/python_project/pythonProject/selenium_3Batch/seleniumForm1.html")
    # driver.get("https://www.iplt20.com/")
    driver.implicitly_wait(9)

    name_element = driver.find_element(By.ID,"name")
    name_element.send_keys("Raaz")

    name_element2 = driver.find_element(By.NAME, "surname")
    name_element2.send_keys("Das")

    date_element = driver.find_element(By.XPATH, "//input[@id='dob']")
    date_element.send_keys("20/11/2025")


    address_element = driver.find_element(By.CLASS_NAME, "addrress-class")
    address_element.send_keys("this is automation testing")

    radio_btn = driver.find_element(By.XPATH, "//input[@id='male']")
    radio_btn.click()
    country = "country"
    select_element = Select(driver.find_element(By.XPATH, f"//select[@id='{country}']"))
    # select_element.select_by_index(3)
    # select_element.select_by_visible_text("United Kingdom")
    select_element.select_by_value("USA")

    agree_btn1 = driver.find_element(By.XPATH, "//input[@id='agree']")
    agree_btn1.click()

    terms_link = driver.find_element(By.XPATH, "//a")
    terms_link.click()
    time.sleep(2)  # Wait for new tab to open
    # terms_linkList = driver.find_elements(By.XPATH, "//a")
    # terms_linkList[3].click()
    # 2. Get window handles
    windows = driver.window_handles
    main_window = windows[0]
    terms_window = windows[1]
    #
    # # 3. Switch to the Terms page window
    # time.sleep(5)
    driver.switch_to.window(terms_window)
    # # 4. Validate page opened by checking title or URL
    current_url = driver.current_url
    print("Opened URL:", current_url)
    assert "policies.google.com" in current_url

    driver.switch_to.window(main_window)

    submit_button = driver.find_element(By.XPATH, "//div/button[@class='submit-btn']")
    submit_button.click()
    time.sleep(2)

    alert = Alert(driver)
    print(f"alertt text {alert.text}")
    alert.accept()




def test_window_handle():
    driver.get("file:/Users/apple/Documents/python_project/pythonProject/selenium_3Batch/seleniumForm1.html")
    driver.implicitly_wait(9)
    # terms_link = driver.find_element(By.XPATH, "//a[@href='https://policies.google.com/terms?hl=en-IN&fg=1']")
    # terms_link = driver.find_element(By.XPATH, "//a[contains(@href, 'policies.google.com/terms')]")
    terms_link = driver.find_element(By.XPATH, "//a")
    terms_link.click()
    time.sleep(2)  # Wait for new tab to open

    # 2. Get window handles
    windows = driver.window_handles
    main_window = windows[0]
    terms_window = windows[1]
    #
    # # 3. Switch to the Terms page window
    # time.sleep(5)
    driver.switch_to.window(terms_window)
    # # 4. Validate page opened by checking title or URL
    current_url = driver.current_url
    print("Opened URL:", current_url)
    assert "policies.google.com" in current_url

    driver.switch_to.window(main_window)


def test_alerts():
    driver.get("https://demoqa.com/alerts")
    # driver.implicitly_wait(9)
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "promtButton").click()
    # confirmButton
    # id="promtButton"

    alert = wait.until(EC.alert_is_present())
    # print("Confirm Alert Text:", alert.text)
    #
    # # alert.accept()  # Click OK
    # alert.dismiss()  # Click OK
    #
    # print("After Clicking OK:", driver.find_element(By.ID, "confirmResult").text)
    alert.send_keys("Testing alerts")
    time.sleep(5)
    alert.accept()  # Click OK



def test_flow_page():
    driver.get("https://flipkart.com")
    driver.implicitly_wait(10)
# '//a[@href="/mobile-phones-store?param=4111&fm=neo%2Fmerchandising&iid=M_3cdd8444-810c-4fef-a0dd-867ce033aced_1_X1NCR146KC29_MC.AH1NTIJZ241Z&cid=AH1NTIJZ241Z"]'
    driver.find_element(By.XPATH, "//a[contains(@href, '/mobile-phones-store-newid?')]").click()


