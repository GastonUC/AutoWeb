#Este script se encargará de abrir una página por si solo y extraer información especifica.
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

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)
driver = webdriver.Safari()

def Image_counter():
    img = driver.find_elements(By.XPATH, "//a[@class='single-image fancybox']")
    Img_count = len(img)
    return Img_count

date = datetime.datetime.now().strftime("%d.%m.%y")
try:
    os.mkdir(f"{date}")
    open(f"{date}/Texto Autos {date}.txt", "x")
except FileExistsError:
    print("Directory already exist.")
    driver.quit()
except OSError as e:
    print(f"Error trying to open file. {e}")
    driver.quit()

for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    name = driver.find_element(By.XPATH, "//h2[@class='section-title']")
    price = driver.find_element(By.XPATH, "//div[@class='price']/span")
    descripcion = driver.find_element(By.XPATH, "//div[@class='col-md-12']/p")

    with open(f"{date}/Texto Autos {date}.txt", "a") as txt:
        txt.write(f"Modelo: {name.text} \nPrecio: {price.text} \nDescripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Auto {str(x+1)}")

    try:
        for y in range(Image_counter()):
            try:
                #Gets Url from images
                url = driver.find_element(By.XPATH, f"//li[@data-slide='{y+1}']/a[@rel='lightbox']/img").get_attribute("src")

                #fetch the content from the url and returns it in bytes. (Binary Response content)
                #Header is mandatory here because the page won't allow to do more than one request for anonymous authentication. So insted, here i pass a Default MDN string.
                response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}).content
                file = open(f"{date}/Auto {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
                file.write(response)
                file.close

                print(f"Imágen {y+1} guardada con éxito")
            except Exception as e:
                print(f"Element not found, {e}")
                driver.quit()
    except Exception as e:
        print(f"Error trying to get Images, {e}")
        driver.quit()
print("Finalizado con éxito!")
driver.quit()