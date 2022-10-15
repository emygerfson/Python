#import urllib
#import urllib.request
#try:
 #   site = urllib.request.urlopen('https://www.tudogostoso.com.br')
#except urllib.error.ULRError:
 #   print('O site esta funcionando')
#else:
 #   print('Não consegui acessar o site')
from selenium import webdriver
driver = webdriver.Chrome()  # Inicia o browser
driver.get('https://www.python.org/')  # Acessar a URL especificada