#Este script se encargará de abrir una página por si solo y extraer información especifica.

# import os
# import time #Just for the sleep, then maybe erase it
# import datetime
# import pyautogui

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# #Se guarda en la variable 'date' la fecha local
# date = datetime.datetime.now().strftime("%d.%m.%y")

# #Cambiar de acuerdo al PATH actual del archivo "chromedriver"
# PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

# #El usuario debe ingresar la url a utilizar.
# #url = input("Ingrese la url: ")
# urls = list(map(str, input("Ingrese las url: ").split()))
# cant = len(urls)
# print("La cantidad de url Ingresadas: "+str(cant))

# #Reconoce el archivo del driver y lo almacena en la variable 'driver'
# driver = webdriver.Chrome(PATH)

# #Crea un txt
# open(f"Texto Autos {date}.txt", "x")

# for x in range(cant):
#     print("URL: "+urls[x]) #Debugging purposes
#     #Ejecuta el driver con la url entregada por el usuario anteriormente.
#     driver.get(urls[x])


#     #def getModelo():
#     try:
#         modelo = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "section-title"))
#         )
#         print("Modelo: "+modelo.text)
#     except:
#         print("No se ha encontrado el modelo del auto ingresado.")

#     #def getPrecio():
#     try:
#         price = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "price"))
#         )
#         print("Precio: "+price.text)
#     except:
#         print("No se ha encontrado el precio del modelo ingresado.")

#     #def getDescripcion():
#     try:
#         descripcion = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-12']/p"))
#         )
#         print("Descripcion: "+descripcion.text)
#     except:
#         print("No se ha encontrado la descripcion del modelo ingresado.")

#     #Abre el txt creado anteriormente y le agrega la informacion obtenida de la pagina. 
#     with open(f"Texto Autos {date}.txt", "a") as txt:
#         txt.write("Precio: " + price.text + "\n" + "Descripcion: " + descripcion.text + "\n" + "\n")
#     print("Insercion de datos en txt Finalizada.")

#     #Se realiza una busqueda para todas las imagenes que tenga la clase 'slide' dentro de la pagina.
#     count = driver.find_elements(By.XPATH, "//li[@class='slide']/a")
#     #Guarda la cantidad de imagenes encontradas.
#     contador = len(count)

#     try:
#         for x in range(contador):
#             try:
#                 img = WebDriverWait(driver, 10).until(
#                     #Realiza busqueda de Imagen en Miniatura.
#                     EC.presence_of_element_located((By.XPATH, "//li[@data-slide='"+str(x+1)+"']/img"))
#                 )
#             except:
#                 print("Imagen Miniatura no encontrada.")
#                 driver.quit()

#             actions = ActionChains(driver)
#             actions.move_to_element(img)
#             actions.click(img)
#             actions.perform()
#             actions.reset_actions()

#             try:
#                 img2 = WebDriverWait(driver, 10).until(
#                     #Realiza busqueda de Imagen en Grande.
#                     EC.presence_of_element_located((By.XPATH, "//li[@data-slide='"+str(x+1)+"']/a[@class='single-image fancybox']/img"))
#                 )
#             except:
#                 print("Imagen Normal no encontrada.")
#                 driver.quit()

#             actions.move_to_element(img2)
#             actions.context_click(img2)
#             actions.perform()
#             actions.reset_actions()
#             time.sleep(1)
#             pyautogui.press('down', presses=8) #presses equivale al total de veces que presionara la KEY
#             pyautogui.press('enter')
#             time.sleep(1) #Espera a que cargue el pop-up

#             fileName = modelo.text #arreglar
#             fName = ""

#             for character in fileName:
#                 if character.isalnum():
#                     fName += character
#             pyautogui.write(fName+" "+str(x+1))
#             pyautogui.press('enter')

#             time.sleep(1)
#             print("Imagen N"+str(x+1)+" guardada.")
#     except:
#         print("Elemento no encontrado")
#         driver.quit()
# print("Proceso finalizado con exito.")
# driver.quit()

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

def Image_counter():
    img = driver.find_elements(By.XPATH, "//a[@class='single-image fancybox']")
    Img_count = len(img)
    return Img_count + 1

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

input_links = list(map(str, input("Ingrese las url: ").split()))
links = len(input_links)

for x in range(links):
    print(f"URL: {input_links[x]}")
    driver.get(input_links[x])

    name = driver.find_element(By.XPATH, "//h2[@class='section-title']")
    price = driver.find_element(By.XPATH, "//div[@class='price']")
    descripcion = driver.find_element(By.XPATH, "//div[@class='col-md-12']/p")

    with open(f"{date}/Texto Autos {date}.txt", "a") as txt:
        txt.write(f"Modelo: {name} \n Precio: {price.text} \n Descripción: {descripcion.text} \n\n")

    os.mkdir(f"{date}/Auto {str(x+1)}")

    try:
        for y in range(Image_counter()):
            try:
                url = driver.find_element(By.XPATH, f"//li[@data-slide='{str(y+1)}']/a[@rel='lightbox']/img").get_attribute("src")

                response = requests.get(url).content
                file = open(f"{date}/Auto {str(x+1)}/{name.text} {str(y+1)}.jpg", "wb")
                file.write(response)
                filr.quit
                print(f"Imágen {y+1} guardada con éxito")
            except Exception as e:
                print(f"Element not found, {e}")
                driver.quit()
    except Exception as e:
        print(f"Error trying to get Images, {e}")
        driver.quit()

print("Finalizado con éxito!")
driver.quit()