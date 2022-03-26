# import AutoWeb
import math


var = 4
pos = []

for x in range(var):
    pos.append(x+1) #Llenando la list con la cantidad de valores entregados por "var"

print("Array completo: ") 
print(pos) #Muestra el contenido del array

med = math.trunc(len(pos)/2)
print(med) #Muestra la mitad del array, en caso de ser float lo aproxima.

if(var == 4) or (var == 6) or (var == 8): #Solución mala al primer cambio de los items.
    med = med - 1

print(med)

posIni = pos[0]
posMed = pos[med]
pos[med] = posIni   #Cambio '1' de posición 0 a posición del medio, guardando el número del medio en variable "posMed" para luego llevarlo a posición 0.
pos[0] = posMed

print("Array with one item sorted: ")
print(pos)

posF = var - 1 #Guarda el index del valor final del array.
posFin = pos[posF] #Guarda el valor de la posición final.
posFinSor = med - 1 #Guarda el index del valor antes del '1'.
pos2 = pos[posFinSor] #Guarda el valor de la posición antes del '1'.
pos[posFinSor] = posFin
pos[posF] = pos2

print("Array with second item sorted:")
print(pos)

### First way to download images

import requests

response = requests.get("https://www.propiedadesarecheta.cl/wp-content/uploads/2022/03/SAM_2527-Large.jpg")
file = open("sample-image.jpg", "wb")
file.write(response.content)
file.close

###
### Second way to download images

import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

runcmd('echo "Hello, World!"', verbose = True)

# runcmd("wget https://www.scrapingbee.com/images/logo-small.png", verbose = True) #Example
runcmd("curl https://www.propiedadesarecheta.cl/wp-content/uploads/2022/03/SAM_2527-Large.jpg > ~/Downloads/image1.jpg")

###


## Páginas abiertas:
# -https://www.geeksforgeeks.org/sort-the-array-in-a-given-index-range/
# -



# ---------------------- Código antiguo areweb en windows ---------------------


# import os
# import time
# import datetime
# import pyautogui

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# date = datetime.datetime.now().strftime("%d.%m.%y")

# PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

# urls = list(map(str, input("Ingrese las url: ").split()))
# cant = len(urls)
# print("La cantidad de url Ingresadas: "+str(cant))

# driver = webdriver.Chrome(PATH)

# open(f"Texto Casas {date}.txt", "x")

# for x in range(cant):
#     print("URL: "+urls[x])
#     driver.get(urls[x])

#     try:
#         sector = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "entry-title"))
#         )
#         print("Sector: "+sector.text)
#     except:
#         print("No se ha encontrado el Sector.")

#     try:
#         precio = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "single-property-price"))
#         )
#         print("Precio: " + precio.text)
#     except:
#         print("No se ha encontrado el Precio.")

#     try:
#         descripcion = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "property-content"))
#         )
#         print("Descripción: " + descripcion.text)
#     except:
#         print("No se ha encontrado la Descripción.")

#     with open(f"Texto Casas {date}.txt", "a") as txt:
#         txt.write(f"Sector: {sector.text} \n" + f"Descripción: {descripcion.text} \n" + f"Precio: {precio.text} \n \n")

#     count = driver.find_elements(By.XPATH, "//ul[@class='slides']/li/a")
#     contador = len(count) - 2
#     print(contador)

#     try:
#         for x in range(contador):
#             try:
#                 point = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, "//li/a[text()='" + str(x+1) + "']"))
#                 )
#             except:
#                 print("Punto no encontrada.")
#                 driver.quit()

#             actions = ActionChains(driver)
#             actions.move_to_element(point)
#             actions.click(point)
#             actions.perform()
#             actions.reset_actions()

#             try:
#                 img = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, "//li[@class='flex-active-slide']"))
#                 )
#             except:
#                 print("Imagen no encontrada.")
#                 driver.quit()

#             actions.move_to_element(img)    
#             actions.context_click(img)
#             actions.perform()
#             actions.reset_actions()
#             time.sleep(1)
#             pyautogui.press('down', presses=8)
#             pyautogui.press('enter')
#             time.sleep(1)
            
#             fileName = sector.text
#             fName = ""

#             for character in fileName:
#                 if character.isalnum():
#                     fName += character
#             pyautogui.write(fName + " " + str(x+1))
#             pyautogui.press('enter')

#             time.sleep(1)
#             print(f"Imagen N{str(x+1)} guardada.")
#     except:
#         print("Elemento no encontrado")
#         driver.quit()

# print("Proceso finalizado con éxito.")
# driver.quit()




# -------------------------------------------------------


# import time
# import pyautogui

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

# url = input("Ingrese la url: ")
# driver = webdriver.Chrome(PATH)

# driver.get(url)

# count = driver.find_elements(By.XPATH, "//div[@class='col-md-3 col-sm-6']/a")
# contador = len(count)
# print(contador)

# time.sleep(10)

# try:
#     close_btn = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span/i[@class='spu-icon spu-icon-close']"))
#     )
#     print("Close btn encontrado.")
# except:
#     print("Close btn no encontrado.")
#     driver.quit()

# actions1 = ActionChains(driver)
# actions1.move_to_element(close_btn)
# actions1.click(close_btn)
# actions1.perform()
# actions1.reset_actions()
# print("close btn apretado.")

# for x in range(contador):
#     try:
#         img = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//div/a[@data-slider-no='" + str(x+1) + "']"))
#         )
#         print("Miniatura encontrada.")
#     except:
#         print("Imagen no encontrada.")
#         driver.quit()

#     actions = ActionChains(driver)
#     actions.move_to_element(img)
#     actions.click(img)
#     actions.perform()
#     actions.reset_actions()
#     print("Miniatura abierta.")

#     time.sleep(2)

#     # try:
#     #     img2 = WebDriverWait(driver, 10).until(
#     #         EC.presence_of_element_located((By.XPATH, "//div[@class='slick-slide slick-current slick-active']/img"))
#     #     )
#     #     print("Imagen fullscreen encontrada.")
#     # except:
#     #     print("Imagen FULLSCREEN no ecnontrada.")
#     #     driver.quit()

#     # try: 
#     #     img2 = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, "//div[@data-slick-index='"+str(x)+"']/img"))
#     # )
#     # except:
#     #     print("fullscreen no encontrado.")
#     #     driver.quit()



#     try:
#         right_arrow = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//div/button[@class='slick-next slick-arrow']"))
#         )
#     except:
#         print("Right arrow not found.")
#         driver.quit()

#     driver.execute_script("arguments[0].click();", right_arrow)
#     time.sleep(2)
#     # actions.move_to_element(right_arrow)
#     # actions.click(right_arrow)
#     # actions.perform()
#     # actions.reset_actions()

#     # driver.find_element(By.XPATH, "//div[@class='slick-slide slick-current slick-active']/img")
#     # driver.switch_to_frame(driver.find_element_by_xpath("//div[@class='modal fade show']"))
#     # img2 = driver.find_element_by_xpath("//div/div/div/div/div/div/div[@class='slick-slide slick-current slick-active']/img")
#     # #driver.find_element(By.ID, "div[@class='property-lightbox']")

#     # actions.move_to_element(img2)
#     # actions.perform() 
#     # actions.reset_actions()
#     # actions.click(img2)
#     # actions.perform()
#     # actions.reset_actions()
#     # actions.context_click(img2)
#     # actions.perform()
#     # actions.reset_actions()

#     # driver.switch_to_default_content()
#     time.sleep(2)
#     driver.quit()

# driver.quit()


### Script anterior de Arecheta
# import os
# import time
# import datetime
# import pyautogui

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# date = datetime.datetime.now().strftime("%d.%m.%y")

# PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

# urls = list(map(str, input("Ingrese las url: ").split()))
# cant = len(urls)
# print("La cantidad de url Ingresadas: "+str(cant))

# driver = webdriver.Chrome(PATH)

# open(f"Texto Casas {date}.txt", "x")

# for x in range(cant):
#     print("URL: "+urls[x])
#     driver.get(urls[x])

#     try:
#         sector = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "page-title"))
#         )
#         print("Sector: "+sector.text)
#     except:
#         print("No se ha encontrado el Sector.")

#     try:
#         precio = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "single-property-price"))
#         )
#         print("Precio: " + precio.text)
#     except:
#         print("No se ha encontrado el Precio.")

#     try:
#         descripcion = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "property-content"))
#         )
#         print("Descripción: " + descripcion.text)
#     except:
#         print("No se ha encontrado la Descripción.")

#     with open(f"Texto Casas {date}.txt", "a") as txt:
#         txt.write(f"Sector: {sector.text} \n" + f"Descripción: {descripcion.text} \n" + f"Precio: {precio.text} \n \n")

#     count = driver.find_elements(By.XPATH, "//ul[@class='slides']/li/a")
#     contador = len(count) - 2
#     print(contador)

#     try:
#         for x in range(contador):
#             try:
#                 point = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, "//li/a[text()='" + str(x+1) + "']"))
#                 )
#             except:
#                 print("Punto no encontrada.")
#                 driver.quit()

#             actions = ActionChains(driver)
#             actions.move_to_element(point)
#             actions.click(point)
#             actions.perform()
#             actions.reset_actions()

#             try:
#                 img = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, "//li[@class='flex-active-slide']"))
#                 )
#             except:
#                 print("Imagen no encontrada.")
#                 driver.quit()

#             actions.move_to_element(img)    
#             actions.context_click(img)
#             actions.perform()
#             actions.reset_actions()
#             time.sleep(1)
#             pyautogui.press('down', presses=8)
#             pyautogui.press('enter')
#             time.sleep(1)
            
#             fileName = sector.text
#             fName = ""

#             for character in fileName:
#                 if character.isalnum():
#                     fName += character
#             pyautogui.write(fName + " " + str(x+1))
#             pyautogui.press('enter')

#             time.sleep(1)
#             print(f"Imagen N{str(x+1)} guardada.")
#     except:
#         print("Elemento no encontrado")
#         driver.quit()

# print("Proceso finalizado con éxito.")
# driver.quit()


### Script de prueba 2 para Arecheta
# import time
# import pyautogui

# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

# url = input("Ingrese la url: ")
# driver = webdriver.Chrome(PATH)

# driver.get(url)

# count = driver.find_elements(By.XPATH, "//div[@class='col-md-3 col-sm-6']/a")
# contador = len(count)
# print(contador)

# time.sleep(10)

# try:
#     close_btn = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span/i[@class='spu-icon spu-icon-close']"))
#     )
#     print("Close btn encontrado.")
# except:
#     print("Close btn no encontrado.")
#     driver.quit()

# actions1 = ActionChains(driver)
# actions1.move_to_element(close_btn)
# actions1.click(close_btn)
# actions1.perform()
# actions1.reset_actions()
# print("close btn apretado.")

# for x in range(contador):
#     try:
#         img = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//div/a[@data-slider-no='" + str(x+1) + "']"))
#         )
#         print("Miniatura encontrada.")
#     except:
#         print("Imagen no encontrada.")
#         driver.quit()

#     actions = ActionChains(driver)
#     actions.move_to_element(img)
#     actions.click(img)
#     actions.perform()
#     actions.reset_actions()
#     print("Miniatura abierta.")

#     time.sleep(2)

#     # try:
#     #     img2 = WebDriverWait(driver, 10).until(
#     #         EC.presence_of_element_located((By.XPATH, "//div[@class='slick-slide slick-current slick-active']/img"))
#     #     )
#     #     print("Imagen fullscreen encontrada.")
#     # except:
#     #     print("Imagen FULLSCREEN no ecnontrada.")
#     #     driver.quit()

#     # try: 
#     #     img2 = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, "//div[@data-slick-index='"+str(x)+"']/img"))
#     # )
#     # except:
#     #     print("fullscreen no encontrado.")
#     #     driver.quit()



#     try:
#         right_arrow = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//div/button[@class='slick-next slick-arrow']"))
#         )
#     except:
#         print("Right arrow not found.")
#         driver.quit()

#     driver.execute_script("arguments[0].click();", right_arrow)
#     time.sleep(2)
#     # actions.move_to_element(right_arrow)
#     # actions.click(right_arrow)
#     # actions.perform()
#     # actions.reset_actions()

#     # driver.find_element(By.XPATH, "//div[@class='slick-slide slick-current slick-active']/img")
#     # driver.switch_to_frame(driver.find_element_by_xpath("//div[@class='modal fade show']"))
#     # img2 = driver.find_element_by_xpath("//div/div/div/div/div/div/div[@class='slick-slide slick-current slick-active']/img")
#     # #driver.find_element(By.ID, "div[@class='property-lightbox']")

#     # actions.move_to_element(img2)
#     # actions.perform() 
#     # actions.reset_actions()
#     # actions.click(img2)
#     # actions.perform()
#     # actions.reset_actions()
#     # actions.context_click(img2)
#     # actions.perform()
#     # actions.reset_actions()

#     # driver.switch_to_default_content()
#     time.sleep(2)
#     driver.quit()

# driver.quit()