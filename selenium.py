from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()



from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search = driver.find_element("name", "q")
search.send_keys("Selenium Testing")

driver.quit()