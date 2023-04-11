# AutoWeb / AreWeb / RomaWeb
Automatización Descarga de imágenes y obtención de datos de la página "Seminuevos"

##Try puppeteer

### Pasos siguientes:
* [ ] Crear funciones para poder manejar todo en "main.py".
* [ ] Crear archivos separados incluyendo un "Main" para ejecución de ciclos, etc.
* [ ] Posiblemente hacer una pequeña UI para el ingreso de URL.
* [x] Creación de carpeta general de lista con nombre "Autos" + fecha del sistema. (El path debería de ser /AutosSeminuevos/Autos x.x.x)
* [x] Crear contador para imágenes.
* [x] Crear ciclo para la descarga de todas las imágenes.
* [x] Creación de ciclo para una lista de URL.
* [x] Creación de Carpeta con modelo del auto.
* [x] Guardado de Info en txt.
* [x] Guardado de Imágenes en carpeta.

### Extras:
* [ ] Añadir funciones para Yapo.cl.
* [x] Ampliar a casas, partiendo por Arecheta.

### Datos útiles:
- ".isalnum()" Para eliminar caracteres especiales
- Para realizar el archivo que contenga toda la lógica tras la descarga, se puede realizar un diccionario que contenga el nombre de las páginas, ya sea (Arecheta, Roma o Seminuevos), junto al PATH indicado para la acción necesitada.
- ~~"import urllib" Para descargas de links~~ (Outdated)
- ~~Para clicks en background: https://forum.uipath.com/t/can-we-have-web-automation-working-in-background/122402/2~~ (Outdated)

## Listado para Testear

* http://seminuevosmag.cl/car/chevrolet/
* http://seminuevosmag.cl/car/mazda-2015/
* http://seminuevosmag.cl/car/nissan-2018/
* http://seminuevosmag.cl/car/hyundai-2017/
* http://seminuevosmag.cl/car/hyundai-2014/
* http://seminuevosmag.cl/car/ssangyong-2017/
* http://seminuevosmag.cl/car/hyundai-2019/

http://seminuevosmag.cl/car/chevrolet/,
http://seminuevosmag.cl/car/mazda-2015/,
http://seminuevosmag.cl/car/nissan-2018/,
http://seminuevosmag.cl/car/hyundai-2017/,
http://seminuevosmag.cl/car/hyundai-2014/,
http://seminuevosmag.cl/car/ssangyong-2017/,
http://seminuevosmag.cl/car/hyundai-2019/

http://seminuevosmag.cl/car/chevrolet/ http://seminuevosmag.cl/car/mazda-2015/ http://seminuevosmag.cl/car/nissan-2018/ http://seminuevosmag.cl/car/hyundai-2014/ http://seminuevosmag.cl/car/ssangyong-2017/ http://seminuevosmag.cl/car/hyundai-2019/

https://romapropiedades.cl/property/inmueble-central/ https://romapropiedades.cl/property/sector-las-cumbres-km-10-norte-poniente/ https://romapropiedades.cl/property/inmueble-sector-norte-pobl-mauricio-braun/ https://romapropiedades.cl/property/sitio-y-tres-cabanas-sector-sur/ https://romapropiedades.cl/property/sector-sur-portal-del-sur/ https://romapropiedades.cl/property/sitio-de-en-1300m2-prolongacion-mardones/ https://romapropiedades.cl/property/propiedad-ubicada-en-brisas-de-agostini/ https://romapropiedades.cl/property/parcela-sector-sur-poniente/ https://romapropiedades.cl/property/parcela-de-8400m2-ojo-bueno/ https://romapropiedades.cl/property/inmueble-sector-sur-poniente/

Structure
<!-- import os
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
    img = driver.find_elements(By.XPATH, "")
    Img_count = len(img)
    return Img_count + 1

date = datetime.datetime.now().strftime("%d.%m.%y")
try:
    os.mkdir(f"{date}")
    open(f"{date}/Texto Autos {date}.txt", "x")
except FileExistsError:
    print("Directory already exist.")
except OSError as e:
    print(f"Error trying to opne file. {e}")
    driver.close()

input_links = list(map(str, input("ingrese las url: ").split()))
links = len(input_links)

for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    name = driver.find_element(By.XPATH, "")
    price = driver.find_element(By.XPATH, "")
    descripcion = driver.find_element(By.XPATH, "")

    with open(f"{date}/Texto Autos {date}.txt", "a") as txt:
        txt.write(f"Modelo: {name} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Auto {str(x+1)}")

    try:
        for y in range(Image_counter()):
            try:
                url = driver.find_element(By.XPATH, "").get_attribute("")

                response = requests.get(url).content
                file = open(f"{date}/Auto {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
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
driver.quit() -->
