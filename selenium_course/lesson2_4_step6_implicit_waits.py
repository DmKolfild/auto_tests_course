from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# Ловим Exception
browser.get("http://suninjuly.github.io/cats.html")

browser.find_element(By.ID, "button")
# NoSuchElementException
