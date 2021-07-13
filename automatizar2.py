import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

print("iniciando prueba con navegador en login sap")
'''
# controlador navegador chrome
controlador = webdriver.Chrome(executable_path=r"C:\pruebas\Driver\chromedriver.exe")
'''

#controlador navegador firefox
controlador=webdriver.Firefox(executable_path=r"C:\pruebas\Driver\geckodriver.exe")

controlador.get("http://127.0.0.1/sap/")
controlador.maximize_window()
time.sleep(1)
usuario = controlador.find_element_by_id("usuario")
usuario.send_keys("admin")
time.sleep(1)
password = controlador.find_element_by_id("password")
password.send_keys("123456")
time.sleep(1)
opcion=controlador.find_element_by_id("opcion")
seleccion=Select(opcion)
time.sleep(1)
seleccion.select_by_value("1")
time.sleep(1)
boton=controlador.find_element_by_id("enviar")
boton.click()
time.sleep(2)
guardar=controlador.find_element_by_id("guardar")
guardar.click()
time.sleep(2)
salir=controlador.find_element_by_id("salir")
salir.click()
time.sleep(2)

print("finalizando prueba")