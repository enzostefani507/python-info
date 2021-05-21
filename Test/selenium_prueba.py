from selenium import webdriver
from time import sleep

browser = webdriver.Chrome("chromedriver")

browser.get("https://www.google.com")
#name="q"
barra_busqueda = browser.find_element_by_name("q")
#me="btnK
barra_busqueda.send_keys("django docs")
boton_buscar = browser.find_element_by_name("btnK")
#sleep(1)
browser.implicitly_wait(5)
boton_buscar.click()

browser.close()