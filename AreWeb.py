#Mac Version
import requests
import io
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
#link: https://www.propiedadesarecheta.cl/propiedades/propiedad-calle-guillermo-tell/

driver.get("https://www.propiedadesarecheta.cl/propiedades/propiedad-calle-guillermo-tell/")

# try:
#     img = driver.find_element(By.XPATH, "//div[@class='col-md-3 col-sm-6']/a")
#     actions = ActionChains(driver)
#     actions.click(img)
#     actions.perform()
#     actions.reset_actions()
#     driver.close()
# except Exception as e:
#     print(f"Error: {e}")
#     driver.close()

time.sleep(10)

try:
    close_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/i[@class='spu-icon spu-icon-close']"))
    )
    print("Close btn encontrado.")
except:
    print("Close btn no encontrado.")
    driver.quit()

actions1 = ActionChains(driver)
actions1.move_to_element(close_btn)
actions1.click(close_btn)
actions1.perform()
actions1.reset_actions()
print("close btn apretado.")

# name = driver.find_element(By.XPATH, "//div[@class='col-md-3 col-sm-6']/a/img")
name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
print(name.text)

price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
print(price.text)

descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")
print(descripcion.text)

# img1 = driver.find_element(By.XPATH, "//div[@class='slick-track']/div[@class='slick-slide']/img")
try:
    img1 = driver.find_element(By.XPATH, "//img[@class='img-fluid']")
    print(img1.text)
except Exception as e:
    print("Element not found " + e)
    driver.close()

# img_link = driver.find_element(By.XPATH, "//div/div[@data-slick-index='0']/img")
# print(img_link.text)
# driver.close()

# for elements in driver.find_elements(By.XPATH, "//div/div[@data-slick-index='0']/img"):
#     print(elements.text)

# try:
#     driver.get("https://www.propiedadesarecheta.cl")
#     print("Visitado con Exito.")

#     driver.close()
# except Exception as e:
#     print(e)
#     driver.close()

    
# makes the browser wait if it can't find an element
# browser.implicitly_wait(10)