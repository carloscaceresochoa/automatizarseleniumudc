import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


def get_controlador(navegador):
    controlador: None
    if (navegador == 1):
        print("Navegador Chrome")
        controlador = webdriver.Chrome(executable_path=r"C:\pruebas\Driver\chromedriver.exe")
    elif (navegador == 2):
        print("Navegador Firefox")
        controlador = webdriver.Firefox(executable_path=r"C:\pruebas\Driver\geckodriver.exe")
    return controlador


def inicio_navegador(navegador, url):
    controlador = get_controlador(navegador)
    controlador.get(url)
    controlador.maximize_window()
    return controlador


def login_sistema(controlador, user, passw, op):
    time.sleep(1)
    usuario = controlador.find_element_by_id("usuario")
    usuario.send_keys(user)
    time.sleep(1)
    password = controlador.find_element_by_id("password")
    password.send_keys(passw)
    time.sleep(1)
    opcion = controlador.find_element_by_id("opcion")
    seleccion = Select(opcion)
    time.sleep(1)
    seleccion.select_by_value(op)
    time.sleep(1)
    boton = controlador.find_element_by_id("enviar")
    boton.click()
    time.sleep(2)


def guardar_usuario(controlador, numident, nombreent, apelent, mailent):
    guardar = controlador.find_element_by_id("guardar")
    guardar.click()
    numid = controlador.find_element_by_name("numid")
    nombre = controlador.find_element_by_name("nombre")
    apellido = controlador.find_element_by_name("apellido")
    mail = controlador.find_element_by_name("mail")
    enviar = controlador.find_element_by_id("enviar")
    mostrar=controlador.find_element_by_id("mostrar")
    time.sleep(1)
    numid.send_keys(numident)
    time.sleep(1)
    nombre.send_keys(nombreent)
    time.sleep(1)
    apellido.send_keys(apelent)
    time.sleep(1)
    mail.send_keys(mailent)
    time.sleep(1)
    enviar.click()
 


controlador = inicio_navegador(1, "http://127.0.0.1/sap")
login_sistema(controlador, "admin", "123456", "1")
guardar_usuario(controlador, "900001", "juan", "lozano", "jl@hotmai.com")
