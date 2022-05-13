#Mac Version
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

#Counter for total images
def Image_counter():
    img = driver.find_elements(By.XPATH, "//div[@class='slick-slide']/img")
    Img_count = len(img)
    return Img_count + 1


date = datetime.datetime.now().strftime("%d.%m.%y")
try:
    os.mkdir(f"{date}")
    open(f"{date}/Texto Casas {date}.txt", "x")
except FileExistsError:
    print("Directory already exist.")
except OSError as e:
    print(f"Error trying to open file. {e}")
    driver.close()

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)
#Loop for all the Urls
for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
    price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
    descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")

    with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
        txt.write(f"Nombre: {name.text} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Propiedad {str(x+1)}")

    try:
        for y in range(Image_counter()):
            try:
                #Gets Url from images
                url = driver.find_element(By.XPATH, "//div[@data-slick-index='" + str(y) + "']/img[@class='img-fluid']").get_attribute("src")
                print(f"Link de la imagen {url}")

                #fetch the content from the url and returns it in bytes. (Binary Response content)
                response = requests.get(url).content
                file = open(f"{date}/Propiedad {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
                file.write(response)
                file.close
                print(f"Imágen {y+1} guardada con éxito")
            except Exception as e:
                print(f"Element not found, {e}")
                driver.close()
    except Exception as e:
        print(f"Error trying to get Images, {e}")
        driver.close()
print("Finalizado con éxito!")
driver.quit()