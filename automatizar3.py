import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

def prueba_login_sma_automatizada():

        print("iniciando prueba con navegador en login sap")

        # controlador navegador chrome
        controlador = webdriver.Chrome(executable_path=r"C:\pruebas\Driver\chromedriver.exe")
        '''
        #controlador navegador firefox
        controlador=webdriver.Firefox(executable_path=r"C:\pruebas\Driver\geckodriver.exe")
        '''
        controlador.get("http://sima.unicartagena.edu.co/login/index.php")
        controlador.maximize_window()
        print("inicio de prueba")
        time.sleep(1)
        username=controlador.find_element_by_id("username")
        password=controlador.find_element_by_id("password")
        boton=controlador.find_element_by_id(("loginbtn"))
        time.sleep(1)
        username.send_keys("124345")
        time.sleep(1)
        password.send_keys("12222")
        time.sleep(1)
        boton.click()
        time.sleep(2)
        print("fin de prueba")

