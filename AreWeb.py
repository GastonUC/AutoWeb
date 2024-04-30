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
# driver.get(input("Write URL: "))

# Counter for total images
# def Image_counter():
#     img = driver.find_elements(By.XPATH, "//div[@class='col-md-3 col-sm-6']")
#     Img_count = len(img)
#     return Img_count
# print(Image_counter())

date = datetime.datetime.now().strftime("%d.%m.%y")
os.mkdir(f"{date}")
open(f"{date}/Texto Casas {date}.txt", "x")

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)
for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    ### Section to obtain info
    description = driver.find_element(By.XPATH, "//div[@class='block-content-wrap']/p") #sometimes the program can found multiple 'p', so the program will return error
    price = driver.find_element(By.XPATH, "//li[@class='item-price']")
    contact = driver.find_element(By.XPATH, "//ul[@class='list-unstyled contact-list']/li/a")
    name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
    # sector = driver.find_element(By.XPATH, "//a[@class='hz-label label label-color-144']").get_attribute("innerText")
    sector = driver.find_element(By.XPATH, "//div[@class='container']/a[2]")

    with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
        txt.write(f"Descripción: {description.text}\nPrecio: {price.text}\nContacto: {contact.text}\n{sector.text}\n\n")

    os.mkdir(f"{date}/Propiedad {str(x+1)}")

    # url = driver.find_elements(By.XPATH, "//div[@class='col-md-3 col-sm-6']/a/img")
    activeImg = driver.find_element(By.XPATH, "//div[@class='slick-slide slick-current slick-active']/img")
    url = driver.find_elements(By.XPATH, "//div[@class='slick-slide']/img")
    url.append(activeImg)
    inc = 0
    try:
        for y in url:
            link = y.get_attribute("data-src")
            inc += 1

            response = requests.get(link).content
            #Header is mandatory here because the page won't allow to do more than one request for anonymous authentication. So insted, here i pass a Default MDN string.
            # response = requests.get(link, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}).content
            file = open(f"{date}/Propiedad {str(x+1)}/{name.text} {inc}.jpg", "wb")
            file.write(response)
            file.close
            print(f"Imágen {inc} guardada con éxito")
    except Exception as e:
        print("Error obteniendo url de imagenes")
        driver.quit()
    print("Finalizado con éxito!")
driver.quit()

#Sector = "document.querySelector('div[class="container"] > a').nextSibling.innerText"
#Sector2 = "document.querySelector('a[class="hz-label label label-color-144"]').innerText"
#activeImg = "document.querySelector('div[class="slick-slide slick-current slick-active"] > img')"
#carrouselImg = "document.querySelectorAll('div[class="slick-slide"] > img')"

#https://www.propiedadesarecheta.cl/propiedades/calle-manuel-tangacis/




# date = datetime.datetime.now().strftime("%d.%m.%y")
# try:
#     os.mkdir(f"{date}")
#     open(f"{date}/Texto Casas {date}.txt", "x")
# except FileExistsError:
#     print("Directory already exist.")
# except OSError as e:
#     print(f"Error trying to open file. {e}")
#     driver.close()

# input_links = list(map(str, input("Ingrese las url: ").split()))
# links = len(input_links)
# #Loop for all the Urls
# for x in range(links):
#     print(f"URL: {input_links[x]}")
#     driver.get(input_links[x])

#     name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
#     price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
#     descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")

#     with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
#         txt.write(f"Nombre: {name.text} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

#     os.mkdir(f"{date}/Propiedad {str(x+1)}")

#     try:
#         for y in range(Image_counter()):
#             try:
#                 #Gets Url from images
#                 url = driver.find_element(By.XPATH, "//a[@data-slider-no='" + str(y) + "']/img").get_attribute("src")
#                 print(f"Link de la imagen {url}")

#                 #fetch the content from the url and returns it in bytes. (Binary Response content)
#                 response = requests.get(url).content
#                 file = open(f"{date}/Propiedad {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
#                 file.write(response)
#                 file.close
#                 print(f"Imágen {y+1} guardada con éxito")
#             except Exception as e:
#                 print(f"Element not found, {e}")
#                 driver.close()
#     except Exception as e:
#         print(f"Error trying to get Images, {e}")
#         driver.close()
# print("Finalizado con éxito!")
# driver.quit()