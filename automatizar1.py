from selenium import webdriver
#controlador navegador chrome
#controlador=webdriver.Chrome(executable_path=r"C:\pruebas\Driver\chromedriver.exe")
#controlador navegador firefox
controlador=webdriver.Firefox(executable_path=r"C:\pruebas\Driver\geckodriver.exe")
controlador.get("http://127.0.0.1/sap/")
controlador.maximize_window()