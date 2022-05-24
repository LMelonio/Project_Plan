from tkinter import Button
from selenium import webdriver    
import time
from selenium.webdriver.common.keys import Keys

# comandos para acessar o site do ge de forma automática

navegador02 = webdriver.Chrome(executable_path=r'C:\Users\Lucas\Desktop\project_plan\chromedriver.exe')
navegador02.maximize_window()
navegador02.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

time.sleep(3)
class botforms():
    def __init__(self):
        self.nome = ('Lucas P Melonio')
        self.tm = ('Corinthians')
        self.classificacao = ('1')
        self.pontuacao = ('14')
        self.navegador = webdriver.Chrome(executable_path=r'C:\Users\Lucas\Desktop\project_plan\chromedriver.exe')
        time.sleep(2)
    # Comandos para acessar o forms de forma automática.
    def preecherforms(self):
        navegador = self.navegador
        navegador.maximize_window()
        navegador.get('https://forms.office.com/r/7UP3THsmUW')
        time.sleep(2)
        nome = navegador.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input')
        nome.send_keys(self.nome)
        time.sleep(2)
        tm = navegador.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
        tm.send_keys(self.tm)
        time.sleep(2)
        classificacao = navegador.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/input')
        classificacao.send_keys(self.classificacao)
        time.sleep(2)
        pontuacao = navegador.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div/input')
        pontuacao.send_keys(self.pontuacao)
        time.sleep(3)
        botao_enviar = navegador.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
        botao_enviar.click()




botforms = botforms()
botforms.preecherforms()

