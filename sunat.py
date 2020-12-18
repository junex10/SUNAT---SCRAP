import time
import re
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = 'https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("no-sandbox")       

browser = webdriver.Chrome()
browser.get(url)

time.sleep(10)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

info = soup.find_all("td", {"class": "calendar-day"})

datos = []

for i in info:
    fechas = i['data-date']
    tmp = []
    
    compras = i.find_all('div', {"class": "normal-all-day"})
    ventas = i.find_all('div', {"class": "pap-all-day"})

    tmp.append({"fecha": fechas})

    for c in compras:
        compra = re.search('[0-9]', c.text)
        compra = compra.string.replace('Compra ', '')
        tmp.append({"compra": compra})
    
    for c in ventas:
        venta = re.search('[0-9]', c.text)
        venta = venta.string.replace('Venta ', '')
        tmp.append({"venta": venta})
    
    datos.append(tmp)

print(datos)
