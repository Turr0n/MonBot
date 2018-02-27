#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import unicodedata
import requests
import json
import os

class pepe():
    '''Pepe me parece un buen nombre como otro cualquiera para esta clase'''
    
    def __init__(self, date):
        '''Configurar los valores iniciales'''

        self.entries = []
        self.base_url = 'http://www.lamoncloa.gob.es/presidente/intervenciones/Paginas/index.aspx'
        self.date = str(date.year)+str(date.month) if date.month >= 10 else str(date.year)+'0'+str(date.month)
        self.path = os.getcwd()+'/archivos/'
        if not os.access(self.path, os.F_OK):
            os.mkdir(self.path)



    def process(self):
        '''Extraer todas las intervenciones en la fecha especificada
            al inicializar la clase creando un diccionario con la siguiente info:
            {fecha, lugar, título, href, texto}
        '''

        html = self.get_web(self.base_url+'?mts='+self.date)
        s = BeautifulSoup(html, 'html.parser')
        self.append(s)

        while True:
            if s.find('div', class_='PaginacionBotonGrande', id='SelectorPaginaSiguiente') and s.find('div', class_='PaginacionBotonGrande', id='SelectorPaginaSiguiente').contents[1].attrs != {}:
                new_url = self.base_url+s.find('div', class_='PaginacionBotonGrande', id='SelectorPaginaSiguiente').find_next('a')['href']
                html = self.get_web(new_url)
                new = BeautifulSoup(html, 'html.parser')
                self.append(new)
            else:
                break
            s = new
        
        print('{} textos...'.format(len(self.entries)))
    
    def append(self, s):
        '''Añadir intervención al diccionario'''

        for element in s.find('ul', class_='buscadorAvanzadoResultados').find_all_next('li'):
            try:
                izq = element.find_next('div', class_='intervencionesSumarioIzquierda')
                fecha =  izq.find_next('p', class_='sumarioFecha').text
                lugar = izq.find_next('p', class_='sumarioMinisterio').text

                link = element.find_next('div', class_='intervencionesSumarioDerecha').find_next('a')

            except AttributeError:
                break
            
            self.entries.append({'fecha':fecha, 'lugar':lugar, 'titulo':link.text, 'href':link['href']})

    def get_docs(self, entry):
        '''Dada una entrada del diccionario crear un archivo json con toda
            la información contenida en el
        '''

        text = self.text('http://www.lamoncloa.gob.es/'+entry['href'])
        entry['text'] = str(text).replace('"', "'")
        entry = {key:self.clean_text(item).decode('utf-8')
                for key, item in entry.items()}   

        fn = self.date+'-'+str(len(os.listdir(self.path))+1)+'.json'
        with open(self.path+fn, 'w') as f:
            json.dump(entry, f)

    def get_web(self, url):
        '''Devolver el contenido de un GET a la url especificada'''

        r = requests.get(url)
        return r.content

    def text(self, url):
        '''Extraer el texto de una intervención'''

        s = BeautifulSoup(self.get_web(url), 'html.parser')
        text = (s.find('div', class_='contenidoTexto')).get_text()
        return text
    
    def clean_text(self, text):
        '''Función para eliminar caracteres potencialmente conflictivos'''

        return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')

if __name__ == '__main__':
    exit()