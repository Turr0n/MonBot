# MonBot
Bot para recopilar las intervenciones publicadas en la página web de La Moncloa de los diferentes presidentes del gobierno. Esta es una herramienta educativa enfocada hacia el NLP y otros proyectos de Machine Learning.

## Úsese con responsabilidad. El autor no se responsabiliza del uso indebido que los usuarios finales hagan de esta herramienta

## Instrucciones de uso
Crear un directorio con el conjunto de intervenciones encontradas para el período especificado. 
```
monbot.py -s yyyymm -e yyyymm
```

Argumentos:
* -s: fecha inicial
* -e: fecha final
* -fn: archivo donde se guardará la información de cada intervención. Por defecto apunta a ```info.json```

Si solo se especifica la fecha inicial se descargaran solamente las intervenciones pertenecientes a ese yyyymm

El texto de cada intervención se alamacenará en un archivo ```.txt``` dentro del directorio ```./archivos```. La información de cada intervención se alamacenará en un archivo ```.json``` donde constará para cada una de ellas:
```
{"titulo", "lugar", "fecha", "id"}
```

El atributo ```id``` corresponde al nombre del fichero de dicha intervención.

## Instalación
```
pip install -r requirements.txt
```

Para que ```selenium``` funcione correctamente es necesario disponer del binario del driver de Firefox. Puedes encontrar más información en: [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/installation.html) y en [stackoverflow.com](https://stackoverflow.com/questions/42204897/how-to-setup-selenium-python-environment-for-firefox)