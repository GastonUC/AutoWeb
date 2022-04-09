### Script Mac Version

import os
import io
import time
import datetime
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()

def Image_counter():
    img = driver.find_elements(By.CLASS_NAME, "swipebox")
    Img_count = len(img)
    return Img_count + 1

date = datetime.datetime.now().strftime("%d.%m.%y")
os.mkdir(f"{date}")
open(f"{date}/Texto Casas {date}.txt", "x")

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)
for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    name = driver.find_element(By.XPATH, "//h1[@class = 'entry-title single-property-title']")
    price = driver.find_element(By.XPATH, "//span[@class = 'single-property-price price']")
    descripcion = driver.find_element(By.XPATH, "//div[@class = 'property-content']/p")

    with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
        txt.write(f"Nombre: {name.text} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Propiedad {str(x+1)}")

    # for a in range(Image_counter()):
    url = driver.find_elements(By.CLASS_NAME, "swipebox") #.get_attribute("href")
    inc = 0
    try:
        for y in url:
            link = y.get_attribute("href")
            inc += 1

            response = requests.get(link).content
            file = open(f"{date}/Propiedad {str(x+1)}/{name.text} {inc}.jpg", "wb")
            file.write(response)
            file.close
            print(f"Imágen {inc} guardada con éxito")
    except Exception as e:
        print(f"Error trying to get Images: {e}")
        driver.close()
    print("Finalizado con éxito!")
driver.quit()