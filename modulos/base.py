import socket
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        ElementNotVisibleException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class web(object):
    def __init__(self):
        print('Inint')
        self.start()
    def start(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #baixa automaticamente o chrome driver
        #self.driver = webdriver.Chrome(executable_path="chromedriver.exe")  # usa chromdriver baixado manualmente
    def nav(self, url):
        self.url = url
        self.driver.get(self.url)
    def quit(self):
        self.driver.quit()
        
    def clicar(self, xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        try:
            WebDriverWait(self.driver, self.tempo).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath)))
        except:
            #self.driver.switch_to_alert().accept()
            WebDriverWait(self.driver, self.tempo).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.location_once_scrolled_into_view
        element.click()

    def apagar(self, xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        WebDriverWait(self.driver, self.tempo).until(
        EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.location_once_scrolled_into_view
        element.clear()
   
    def preencher(self, xpath, tempo, texto, click='off'):
        self.xpath = xpath
        self.tempo = tempo
        self.texto = texto
        self.click = click
        WebDriverWait(self.driver, self.tempo).until(
        EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.location_once_scrolled_into_view
        if self.click in 'on':
            self.clicar(self.xpath, self.tempo)
        else:
            pass
        element.send_keys(texto)
        while texto in self.driver.find_element(By.XPATH, self.xpath).text:
            web.apagar(self, xpath, tempo)
            element.send_keys(self.texto)
        
    def ler(self, xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        WebDriverWait(self.driver, self.tempo).until(
        EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.location_once_scrolled_into_view
        return element.text
    
    def localizar(self, xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        WebDriverWait(self.driver, tempo).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
        self.element = self.driver.find_element(By.XPATH, xpath)
        return self.element
        
    def localizarv(self,xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        WebDriverWait(self.driver, tempo).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
        self.element = self.driver.find_elements(By.XPATH, xpath)
        return self.element
        
    
    def titulo(self, titulo1):
        self.titulo1 = titulo1
        assert self.titulo in self.driver.title      

    def teste_conexao(self):
        try:
            # teste de conexão
            self.socket.create_connection(("www.google.com", 80))
            return True
        except:
            self.teste_conexao()

    def framep(self):
        self.driver.switch_to_default_content()

    def framex(self, xpath, tempo):
        self.xpath = xpath
        self.tempo = tempo
        WebDriverWait(self.driver, self.tempo).until(
        EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        self.driver.switch_to.frame(element)
