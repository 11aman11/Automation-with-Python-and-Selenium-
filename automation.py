from selenium import webdriver

chromeBrowser = webdriver.Chrome()
from selenium.webdriver.common.by import By
# chromeBrowser = webdriver.Chrome()
# print(chromeBrowser)
chromeBrowser.maximize_window()
chromeBrowser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
#print("Selenium Easy Demo" in chromeBrowser.title)
assert "Selenium Easy Demo" in chromeBrowser.title
# buttonText=chromeBrowser.find_element("btn-default")
# print(buttonText.get_attribute('innerHTML'))
assert "Show Message" in chromeBrowser.page_source

userMessage=chromeBrowser.find_element(by=By.ID,value="user-message")
userMessage.clear()
userMessage.send_keys("I am awesome")

showMessageButton = chromeBrowser.find_element(By.CLASS_NAME,"btn-default")
showMessageButton.click()