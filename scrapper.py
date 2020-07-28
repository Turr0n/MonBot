from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import requests

from typing import Sequence

import json
import os


class first_element_has_changed(object):
    '''
        Espera hasta que aparecen las nuevas entradas comprobando el href
        del primer link contra el primero de la ultima tanda de los ya analizados
    '''

    def __init__(self, locator, prev_el_href: str):
        self.locator = locator
        self.prev_el_href = prev_el_href

    def __call__(self, driver):
        try:
            current_href = driver.find_element(*self.locator).get_attribute("href")
        except:
            return "no more" # We have to return something that evalutes as truthy but no True itself.
                
        if self.prev_el_href != current_href:
            return True
        else:
            return False



class pepe():
    '''Pepe me parece un buen nombre como otro cualquiera para esta clase'''
    
    def __init__(self):
        '''Configurar los valores iniciales'''

        opts = Options()
        opts.set_headless()
        self.driver = webdriver.Firefox(options = opts)

        self.base_url = "http://www.lamoncloa.gob.es/presidente/intervenciones/Paginas/index.aspx"
        self.path = os.getcwd()+"/archivos/"
        self.entries = []
        self.ids = set()
        
        if not os.access(self.path, os.F_OK):
            os.mkdir(self.path)


    def process(self, date: str):
        '''
            Extraer todas las intervenciones en la fecha especificada
            al inicializar la clase creando un diccionario con la siguiente info:
            {fecha, lugar, título, href, texto}
        '''

        def find(selector: str, many: bool = False):
            if (many): return self.driver.find_elements_by_css_selector(selector)
            else: return self.driver.find_element_by_css_selector(selector)


        self.driver.get(f"{ self.base_url }?mts={ date }")
        
        page = 1
        while True:
            entries = find("li.advanced-new a", True)
            
            print(f"New entries: { len(entries) }")
            
            for entry in entries:
                self.ingest(entry.get_attribute("href")) 

            old_first_href = entries[0].get_attribute("href")
            self.driver.execute_script(f"DoListItems('1;{ page + 1 }')")

            more = WebDriverWait(self.driver, 10, 0.25).until(
                first_element_has_changed((By.CSS_SELECTOR, "li.advanced-new a"), old_first_href)
            )

            if (more != True): break

            page += 1
        
        print(f"Processed entries: { len(self.ids) }")
    

    def ingest(self, url: str):
        '''Procesado de intervenciones. Volcado de info al diccionario y el texto a un fichero'''

        id_ = url.split("/")[-1][:-5]
        print(f"Processing entry: { id_ }")
        
        if (id_ in self.ids):
            print(f"Entry { id_ } has already been processed!")
            return
        else:
            self.ids.add(id_)

        title, place, date, text = self.text(url)
        self.entries.append(
            {
                "titulo": title,
                "lugar": place,
                "fecha": date,
                "id": id_
            }
        )

        with open(f"{ self.path }{ id_ }.txt", "w", encoding="utf-8") as f:
            f.write(text)


    def get_web(self, url: str) -> str:
        '''Devolver el contenido de un GET a la url especificada'''

        r = requests.get(url)
        return r.text


    def text(self, url: str) -> Sequence[str]:
        '''Extraer el título, lugar, fecha y texto de una intervención'''

        s = BeautifulSoup(self.get_web(url),"html.parser")
        title = s.find("h1", id="h1Title").get_text()

        aux = s.find("p", class_="date").get_text().split(", ")
        place, date = aux if (len(aux) == 2) else (", ".join(aux[:-1]), aux[-1])

        text = s.find("div", id="MainContent").get_text()

        return title, place, date, text

    
    def dump(self, fn: str):
        '''Guarda el diccionario y cierra el driver'''
        print(self.entries)

        with open(fn, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, ensure_ascii=False)

        self.driver.quit()


if __name__ == "__main__":
    exit()