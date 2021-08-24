#Este script se encargará de abrir una página por si solo y extraer información especifica.

import os
import time #Just for the sleep, then maybe erase it
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Cambiar de acuerdo al PATH actual del archivo "chromedriver"
PATH = "/Users/Win10Pro/Documents/AutoWeb/chromedriver"

#El usuario debe ingresar la url a utilizar.
url = input("Ingrese la url: ")

#Reconoce el archivo del driver y lo almacena en la variable 'driver'
driver = webdriver.Chrome(PATH)
#Ejecuta el driver con la url entregada por el usuario anteriormente.
driver.get(url)

#def getModelo():
try:
    modelo = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "section-title"))
    )
    print("Modelo: "+modelo.text)
except:
    print("No se ha encontrado el modelo del auto ingresado.")

#def getPrecio() ah:
try:
    price = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    )
    print("Precio: "+price.text)
except:
    print("No se ha encontrado el precio del modelo ingresado.")

#def getDescripcion():
try:
    descripcion = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-12']/p"))
        #Otherwise /html/body/div/div/div/div/div/div/main/article/div/div/p
    )
    print("Descripcion: "+descripcion.text)
except:
    print("No se ha encontrado la descripcion del modelo ingresado.")

#Se realiza una busqueda para todas las imagenes que tenga la clase 'slide' dentro de la pagina.
count = driver.find_elements(By.XPATH, "//li[@class='slide']/a")
#Guarda la cantidad de imagenes encontradas.
contador = len(count)
#print(contador) #Para motivos Debug.


# if(contador == 3):
#     ar = [3,1,2]
# elif(contador == 4):
#     ar = [4,1,2,3]
# elif(contador == 5):
#     ar = [4,5,1,2,3]
# elif(contador == 6):
#     ar = [5,6,1,2,3,4]
# elif(contador == 7):
#     ar = [5,6,7,1,2,3,4]
# elif(contador == 8):
#     ar = [6,7,8,1,2,3,4,5]
# elif(contador == 9):
#     ar = [6,7,8,9,1,2,3,4,5]
# else:
#     print("Error, please check the code.")

try:
    for x in range(contador):
        try:
            img = WebDriverWait(driver, 10).until(
                #EC.presence_of_element_located((By.XPATH, "//li[@data-slide='"+str(ar[x])+"']/img"))
                #Realiza busqueda de Imagen en Miniatura.
                EC.presence_of_element_located((By.XPATH, "//li[@data-slide='"+str(x+1)+"']/img"))
            )
        except:
            print("Imagen Miniatura no encontrada.")
            driver.quit()

        actions = ActionChains(driver)
        actions.move_to_element(img)
        actions.click(img)
        actions.perform()
        actions.reset_actions()

        try:
            img2 = WebDriverWait(driver, 10).until(
                #Realiza busqueda de Imagen en Grande.
                EC.presence_of_element_located((By.XPATH, "//li[@data-slide='"+str(x+1)+"']/a[@class='single-image fancybox']/img"))
            )
        except:
            print("Imagen Normal no encontrada.")
            driver.quit()

        actions.move_to_element(img2)
        actions.context_click(img2)
        actions.perform()
        actions.reset_actions()
        time.sleep(1)
        # for z in range(7):
        #     pyautogui.press('down')
        pyautogui.press('down', presses=8) #presses equivale al total de veces que presionara la KEY
        pyautogui.press('enter')
        time.sleep(1) #Espera a que cargue el pop-up

        fileName = modelo.text #arreglar
        fName = ""

        for character in fileName:
            if character.isalnum():
                fName += character
        pyautogui.write(fName+" "+str(x+1))
        pyautogui.press('enter')

        time.sleep(1)
        print("Imagen N"+str(x+1)+" guardada.")
except:
    print("Elemento no encontrado")
    driver.quit()
        
print("Proceso finalizado con exito.")
driver.quit()