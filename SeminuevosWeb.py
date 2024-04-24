import os
import datetime
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()

date = datetime.datetime.now().strftime("%d.%m.%y")
if(os.path.exists(f"{date}")):
    print("La Carpeta ya existe.")
    print("Quieres sobrescribir la carpeta?")
    answer = input("Y/N: ").lower()
    if(answer == "y"):
        shutil.rmtree(f"{date}")
        print("Carpeta eliminada.")
    elif(answer == "n"):
        print("Saliendo...")
        driver.quit()
    else:
        print("Tecla inválida. Saliendo...")
        driver.quit()
os.mkdir(f"{date}")
open(f"{date}/Texto Seminuevos {date}.txt", "x")
with open(f"{date}/Texto Seminuevos {date}.txt", "a") as txt:
    txt.write("Los datos adicionales son extras en caso de que las descripciones no tengan suficiente información.\n\n")

input_links = list(map(str, input("Ingrese las url: ").split()))
# links = len(input_links)
for link in input_links:
    driver.get(link)

    descripcion = driver.find_element(By.XPATH, "//div[@class='col-md-12']/p").get_attribute("innerText")
    precio = driver.find_element(By.XPATH, "//div[@class='price']/span").get_attribute("innerText")
    nombre = driver.find_element(By.XPATH, "//h2[@class='section-title']").get_attribute("innerText")
    extras = driver.find_elements(By.XPATH, "//ul[@class='data-list']/li")
    km = extras[3].get_attribute("innerText")

    # print(f"Descripción: {descripcion}\nPrecio: {precio}\nNombre: {nombre}\n")
    with open(f"{date}/Texto Seminuevos {date}.txt", "a") as txt:
        txt.write(f"Descripción: {descripcion}\nPrecio: {precio}\nNombre: {nombre}\nDatos adicionales: {km}\n\n")

    os.mkdir(f"{date}/Auto {str(input_links.index(link)+1)}") #This is to create a folder with the name of the property, should get it correctly
    url_imagenes = driver.find_elements(By.XPATH, "//ul[@id='car_slider']/div[@class='slidesContainer']/li/a/img")
    inc = 0

    try:
        for url in url_imagenes:
            image_link = url.get_attribute("src")
            # print(f"URL de la imagen: {image_link}") # Debugging
            inc += 1 # Incrementador
            response = requests.get(image_link, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}).content
            # print(f"respuesta binary: {response}")
            file = open(f"{date}/Auto {str(input_links.index(link)+1)}/{nombre} {inc}.jpg", "wb")
            file.write(response)
            file.close
            print(f"Imágen {inc} guardada con éxito")
    except Exception as e:
        # print("Error obteniendo url de imagenes")
        print(f"Error en descarga: {e}")
        driver.quit()
    print("Finalizado con éxito!")
driver.quit()

#descripcion = "document.querySelector('div[class="col-md-12"] > p').innerText"
#precio = "document.querySelector('div[class="price"] > span').innerText"
#nombreAlternativo = "document.querySelector('h2[class="section-title"]').innerText"
#nombre = "document.querySelector('div[class="col-md-8"] > h2[class="section-title"]').innerText" has extra spaces for the span embeded
#imagenes = "document.querySelectorAll('ul[id="car_slider"] > div[class="slidesContainer"] > li')"
#km = "document.querySelectorAll('ul[class="data-list"] > li')"