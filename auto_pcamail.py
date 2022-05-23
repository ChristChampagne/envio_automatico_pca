from os import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import json
import time
import sys

# Christian Eduardo Rodriguez Perez. 5 feb 2022

# Abrir el archivo JSON
with open('data2.json') as f:

    # Importar el archivo en modo lectura
	data = json.loads(f.read())

# Recorrer los datos del JSON
	for datos in data:
            # Asignar los valores del JSON a una variable
            nombre = datos['apellido'] + " " + datos['apellido2']
            email = datos['email']
            telefono = datos['telefono']
            mensaje = datos['mensaje']
            # Opciones para que corra el navegador junto con Selenium.
            options = Options()
            options.add_experimental_option("detach", True)
            
            # Localización de Brave
            options.binary_location = "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\Brave.exe"

            # Iniciaizar el driver para selenium con la variable navegador
            navegador = webdriver.Chrome(options = options, executable_path=r'.\chromedriver.exe')

            # Abrir el navegador en la url del formulario
            navegador.get('http://carrillodavid.utdgrupoti.com/cursosCD/contacto.php')

            # localizar elementos del formulario por su ID e ingresarle las variables extraidas del JSON
            navegador.find_element_by_id("name").send_keys(str(nombre))
            navegador.find_element_by_id("email").send_keys(str(email))
            navegador.find_element_by_id("phone").send_keys(str(telefono))
            navegador.find_element_by_id("message").send_keys(str(mensaje))

            # Hacer un enter en el formulario
            navegador.find_element_by_id("enviar").send_keys(Keys.RETURN)
            
            # Una vez ingresados los datos cerrar el navegador
            navegador.close()

            # Esperar 3 segundos para volver a insertar datos
            time.sleep(1)
            
            system("cls")