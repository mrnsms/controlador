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
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy
from webdriver_manager.chrome import ChromeDriverManager



class web(object):

    #driver = webdriver.Chrome()
    #driver.quit()
    def __init__(self):
        print('Inint')
        self.start()
    def start(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #linux
        #self.driver = webdriver.Chrome(executable_path="chromedriver.exe") #windows
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
   
    def preencher(self, xpath, tempo, texto):
        self.xpath = xpath
        self.tempo = tempo
        self.texto = texto
        WebDriverWait(self.driver, self.tempo).until(
        EC.element_to_be_clickable((By.XPATH, self.xpath)))
        element = self.driver.find_element(By.XPATH, self.xpath)
        element.location_once_scrolled_into_view
        while texto in self.driver.find_element(By.XPATH, self.xpath).text:
            web.apagar(self, xpath, tempo)
            element.send_keys(self.texto)
        element.send_keys(texto)

        
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
    
    def titulo(self, titulo1):
        self.titulo1 = titulo1
        assert self.titulo in self.driver.title
        
    def abrir_planilha(self, planilha='Pasta1.xls'):
        self.planilha = planilha
        self.rb = open_workbook(planilha)
        self.rs = self.rb.sheet_by_index(0)
        self.wb = copy(self.rb)
        self.ws = self.wb.get_sheet(0)
        
    def fechar_planilha(self, planilha):
        self.planilha = planilha
        self.wb.save(self.planilha)

    def teste_conexao(self):
        try:
            # teste de conexão
            self.socket.create_connection(("www.google.com", 80))
            return True
        except:
            self.teste_conexao()

    def framep(self):
        self.driver.switch_to_default_content()
