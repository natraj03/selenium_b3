from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


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


    submit_button = driver.find_element(By.XPATH, "//div/button[@class='submit-btn']")
    submit_button.click()

