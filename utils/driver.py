from selenium import webdriver
from selenium.webdriver.chrome.service import Service



def getChromeDriver():
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
    return driver

def getFirefoxDriver():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment to run without opening browser
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    #
    # # ✅ Use Service() with path to chromedriver
    # service = Service("/Users/apple/Documents/chromedriver/14chromedriver_mac64/chromedriver")
    # driver = webdriver.Chrome(service=service, options=options)

    return webdriver.Firefox()