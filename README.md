# MonBot
Bot para recopilar las intervenciones publicadas en la página web de La Moncloa de los diferentes presidentes del gobierno. Esta es una herramienta educativa enfocada hacia el NLP y otros proyectos de Machine Learning.

## Úsese con responsabilidad. El autor no se responsabiliza del uso indebido que los usuarios finales hagan de esta herramienta

##Instrucciones de uso
Crear un directorio con el conjunto de intervenciones encontradas para el período especificado. 
'''
monbot.py -s yyyymm -e yyyymm
'''

Argumentos:
* -s fecha inicial
* -e fecha final

Si solo se especifica la fecha inicial se descargaran solamente las intervenciones pertenecientes a ese yyyymm

Cada intervención es almacenada en un archivo JSON individual con la siguiente información en forma de objeto (diccionario en Python):
'''
{fecha, lugar, titulo, href, texto}
'''

##Ejemplo
'''
{
	"href": "/presidente/intervenciones/Paginas/2013/prar190513elcorreo.aspx",
	"lugar": "Articulo de Mariano Rajoy publicado en el \"El Correo\"",
	"fecha": "19/05/2013",
	"titulo": "Gracias, Antonio",
	"text": "\nHace treinta anos que milito en el Partido Popular y cada dia que pasa es mayor mi admiracion y mi agradecimiento hacia las decenas de miles de militantes que han hecho de este partido uno de los mas grandes de Europa.\nEn el caso de los militantes del Partido Popular en el Pais Vasco, la gratitud y la admiracion son mayores si cabe. Han vivido anos terribles de sufrimiento y acoso continuado. Han sabido sobreponerse a los crueles asesinatos de companeros, al aislamiento y al miedo. Han levantado la bandera del PP, de Espana y de la libertad en las circunstancias mas dificiles que nadie pueda imaginar.\nHoy, cuando todo el mundo nos pide a los politicos ejemplaridad y dedicacion generosa, yo miro a mis companeros del Pais Vasco y a los de otros partidos politicos que han compartido con ellos la lucha por la libertad y me pregunto que mas ejemplaridad se puede pedir a un politico. Dificilmente se podra encontrar un ejemplo de mayor entrega en la defensa desinteresada de unos ideales.\nAntonio Basagoiti, a quien hoy despedimos, es uno de esos politicos ejemplares que se forjo en esa dura, pero nobilisima batalla. Probablemente en otras circunstancias ni se hubiera dedicado a la politica, pero su estatura moral no le dejo otra opcion. Podia haber vivido muy bien y muy comodo mirando hacia otro lado, pero no quiso; miro de frente a la durisima realidad de su tierra y se puso manos a la obra para cambiarla.\nAntonio Basagoiti ha dado la batalla y lo ha hecho siempre con una sonrisa, con la seguridad de quien cree profundamente en lo que hace, sin dar mayor importancia a su indudable ejemplo civico. Alegre, natural y desenfadado, si yo tuviera que escoger a una persona con quien ilustrar el concepto de inteligencia emocional, esa persona seria, sin duda, Antonio Basagoiti. Y esto que hoy afirmo lo comparten sus companeros de partido, sus rivales politicos y los medios de comunicacion que ya estan echando en falta esos titulares frescos y certeros que siempre ha sabido obsequiarles.\nA partir de ahora seran otros quienes disfruten de su cordialidad y su buen hacer, de su lealtad y su coraje. En nombre de todos los militantes del Partido Popular, yo solo puedo darle las gracias por la labor ingente que ha hecho para esta formacion politica y desearle lo mejor en la nueva vida que ahora comienza. Nuestro partido pierde, sin duda, un personaje sobresaliente y lleno de futuro. Pero alla donde este y a donde le lleven sus sobrados meritos, Antonio Basagoiti sera siempre un orgullo para todos nosotros. Una persona de bien, un espanol ejemplar y un vasco de los que ennoblecen esta maravillosa tierra.\nNOTA: Articulo publicado con la autorizacion de 'El Correo'.\n"
}
'''