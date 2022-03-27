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

#link: https://www.propiedadesarecheta.cl/propiedades/propiedad-calle-guillermo-tell/
# driver.get("https://www.propiedadesarecheta.cl/propiedades/calle-zenteno-cerro-primavera/")
# driver.get("https://www.propiedadesarecheta.cl/propiedades/depto-4o-piso-condominio-san-ignacio-1/")

# try:
#     close_btn = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//span/i[@class='spu-icon spu-icon-close']"))
#     )
#     actions1 = ActionChains(driver)
#     actions1.move_to_element(close_btn)
#     actions1.click(close_btn)
#     actions1.perform()
#     actions1.reset_actions()
# except Exception as e:
#     print("Close btn no encontrado. " + e)
#     driver.quit()

driver = webdriver.Safari()

def Image_counter():
    img = driver.find_elements(By.XPATH, "//div[@class='slick-slide']/img")
    Img_count = len(img) #Contador
    #print(f"Contador de imagenes: {Img_count}") #Imprime el total de imagenes que hay
    return Img_count + 1

# print(Image_counter()) debugging purposes

# def fill_txt():
#     name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
#     price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
#     descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")

#     with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
#         txt.write(f"Nombre: {name.text} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")
#     return name.text


date = datetime.datetime.now().strftime("%d.%m.%y")
os.mkdir(f"{date}")
open(f"{date}/Texto Casas {date}.txt", "x")

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)
for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    # fill_txt()
    name = driver.find_element(By.XPATH, "//div[@class='page-title']/h1")
    price = driver.find_element(By.XPATH, "//ul[@class='item-price-wrap hide-on-list']/li")
    descripcion = driver.find_element(By.XPATH, "//div[@class='block-wrap']/div[@class='block-content-wrap']/p")

    with open(f"{date}/Texto Casas {date}.txt", "a") as txt:
        txt.write(f"Nombre: {name.text} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Propiedad {str(x+1)}")
    # try:
    #     name = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1"))
    #     )
    # except Exception as e:
    #     print(f"Error: {e}")

    try:
        for y in range(Image_counter()):
            try:
                url = driver.find_element(By.XPATH, "//div[@data-slick-index='" + str(y) + "']/img[@class='img-fluid']"). get_attribute("src") #Obtiene el link de las imagenes
                #print(url) #Muestra por pantalla el link

                response = requests.get(url).content #fetch the content from the url and returns it in bytes. (Binary Response content)
                file = open(f"{date}/Propiedad {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
                file.write(response)
                file.close
                print(f"Imágen {y+1} guardad con éxito")
            except Exception as e:
                print(f"Element not found, {str(e)}")
                driver.close()
    except Exception as e:
        print(f"Error trying to get Images: {e}")
        driver.close()
print("Finalizado con éxito!")
driver.quit()