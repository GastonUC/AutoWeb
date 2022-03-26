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

# driver.get("https://www.propiedadesarecheta.cl/propiedades/calle-los-maderos-altos-del-bosque/")
driver.get("https://www.propiedadesarecheta.cl/propiedades/calle-zenteno-cerro-primavera/")
# driver.get("https://www.propiedadesarecheta.cl/propiedades/depto-4o-piso-condominio-san-ignacio-1/")


time.sleep(10)

try:
    close_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/i[@class='spu-icon spu-icon-close']"))
    )
except Exception as e:
    print("Close btn no encontrado." + e)
    driver.quit()

actions1 = ActionChains(driver)
actions1.move_to_element(close_btn)
actions1.click(close_btn)
actions1.perform()
actions1.reset_actions()


name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
print(name.text)

price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
print(price.text)

descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")
print(descripcion.text)

def Image_counter():
    img = driver.find_elements(By.XPATH, "//div[@class='slick-slide']/img")
    Img_count = len(img) #Contador
    print(f"Contador de imagenes: {Img_count}") #Imprime el total de imagenes que hay
    return Img_count + 1

# print(Image_counter()) debugging purposes

try:
    for x in range(Image_counter()):
        try:
            img1 = driver.find_element(By.XPATH, "//div[@data-slick-index='" + str(x) + "']/img[@class='img-fluid']"). get_attribute("src") #Obtiene el link de las imagenes
            print(img1)
        except Exception as e:
            print(f"Element not found, {str(e)}")
            driver.close()
except Exception as e:
    print(f"Error trying to get Images: {e}")
    driver.close()

driver.quit()

# img_link = driver.find_element(By.XPATH, "//div/div[@data-slick-index='0']/img")
# print(img_link.text)
# driver.close()

# for elements in driver.find_elements(By.XPATH, "//div/div[@data-slick-index='0']/img"):
#     print(elements.text)

# makes the browser wait if it can't find an element
# browser.implicitly_wait(10)