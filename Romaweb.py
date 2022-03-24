import os
import time
import datetime
import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

date = datetime.datetime.now().strftime("%d.%m.%y")

PATH = "/Users/PbmEditor/Documents/Vscode/AutoWeb/chromedriver"

urls = list(map(str, input("Ingrese las url: ").split()))
cant = len(urls)
print("La cantidad de url Ingresadas: "+str(cant))

driver = webdriver.Chrome(PATH)

open(f"Texto Casas {date}.txt", "x")

for x in range(cant):
    print("URL: "+urls[x])
    driver.get(urls[x])

    try:
        sector = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "entry-title"))
        )
        print("Sector: "+sector.text)
    except:
        print("No se ha encontrado el Sector.")

    try:
        precio = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "single-property-price"))
        )
        print("Precio: " + precio.text)
    except:
        print("No se ha encontrado el Precio.")

    try:
        descripcion = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "property-content"))
        )
        print("Descripción: " + descripcion.text)
    except:
        print("No se ha encontrado la Descripción.")

    with open(f"Texto Casas {date}.txt", "a") as txt:
        txt.write(f"Sector: {sector.text} \n" + f"Descripción: {descripcion.text} \n" + f"Precio: {precio.text} \n \n")

    count = driver.find_elements(By.XPATH, "//ul[@class='slides']/li/a")
    contador = len(count) - 2
    print(contador)

    try:
        for x in range(contador):
            try:
                point = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//li/a[text()='" + str(x+1) + "']"))
                )
            except:
                print("Punto no encontrada.")
                driver.quit()

            actions = ActionChains(driver)
            actions.move_to_element(point)
            actions.click(point)
            actions.perform()
            actions.reset_actions()

            try:
                img = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//li[@class='flex-active-slide']"))
                )
            except:
                print("Imagen no encontrada.")
                driver.quit()

            actions.move_to_element(img)    
            actions.context_click(img)
            actions.perform()
            actions.reset_actions()
            time.sleep(1)
            pyautogui.press('down', presses=8)
            pyautogui.press('enter')
            time.sleep(1)
            
            fileName = sector.text
            fName = ""

            for character in fileName:
                if character.isalnum():
                    fName += character
            pyautogui.write(fName + " " + str(x+1))
            pyautogui.press('enter')

            time.sleep(1)
            print(f"Imagen N{str(x+1)} guardada.")
    except:
        print("Elemento no encontrado")
        driver.quit()

print("Proceso finalizado con éxito.")
driver.quit()