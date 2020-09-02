#Este script se encargará de abrir una página por si solo y extraer cierta información.

import os
import time #Just for the sleep, then maybe erase it
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/Users/Gacox/Desktop/AutoWeb/chromedriver"

url = input("Ingrese la url: ")

driver = webdriver.Chrome(PATH)
driver.get(url)

def getModelo():
    try:
        modelo = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "section-title"))
        )
        print("Modelo: "+modelo.text)
    except:
        print("No se ha encontrado el modelo del auto ingresado.")

def getPrecio():
    try:
        price = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
        print("Precio: "+price.text)
    except:
        print("No se ha encontrado el precio del modelo ingresado.")

def getDescripcion():
    try:
        descripcion = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-12']/p"))
            #Otherwise /html/body/div/div/div/div/div/div/main/article/div/div/p
        )
        print("Descripcion: "+descripcion.text)
    except:
        print("No se ha encontrado la descripcion del modelo ingresado.")

def otraWea():
    try:
        img = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-slide='2']/a"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(img)
        actions.context_click(img)
        actions.perform()
        for x in range(7):
            pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)

        fileName = modelo.text #arreglar
        fName = ""

        for character in fileName:
            if character.isalnum():
                fName += character
        pyautogui.write(fName)
        pyautogui.press('enter')

        time.sleep(1) #Posiblemente falle con un nuevo link
    except:
        print("link no encontrado")
        driver.quit()

driver.quit()