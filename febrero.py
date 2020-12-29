import time
import re
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

driver_exe = 'chromedriver'

browser = webdriver.Chrome(driver_exe)
browser.minimize_window()
url = 'https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'
browser.get(url)

datos = []

febrero = []

def scrap(info, mes, varmes):

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
            
        varmes.append(tmp) 

    datos.append({mes: varmes})

x = 0

while x != 1:

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    com = soup.find_all('div', {"class": "normal-all-day"})

    if len(com) > 0:
        x = 1
    else:
        browser.refresh()
        time.sleep(10)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)

link = browser.find_elements_by_class_name("js-cal-prev")[0]
link.click()
time.sleep(5)
k = 0

while k != 1:

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    com = soup.find_all('div', {"class": "normal-all-day"})

    if len(com) > 0:
        k = 1
    else:
        browser.refresh()
        
        time.sleep(10)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)

        link = browser.find_elements_by_class_name("js-cal-prev")[0]
        link.click()
        time.sleep(5)


html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

info = soup.find_all("td", {"class": "calendar-day"})

scrap(info, 'febrero', febrero)

print(datos)