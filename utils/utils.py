def open_flipkart_website(driver, path=None):
    url = "https://flipkart.com"
    url = url if path == None else url +  path
    driver.get(url)
    driver.implicitly_wait(10)