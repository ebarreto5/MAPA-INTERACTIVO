Resumen
El contenido de este proyecto es la forma y las características del programa que desarrollaremos. Lo que se espera lograr en este proyecto es de poder mapear todas las coordenadas de los dispositivos de luminaria publica (Previamente ya obtenidas)
existentes en la cabecera municipal de Coquimatlán,
así como las características que tiene cada una
actualmente. El fin de este proyecto es la de generar
y actualizar la información con la que cuenta la
entidad respecto a el alumbrado público.
Palabras Clave: Coordenadas-Mapa-Lamparas-
G.P.S.
Abstract
The content of this project is the form and
characteristics of the program that we will develop.
What is expected to be achieved in this project is to
be able to map all the coordinates of the public
luminaire devices (previously already obtained)
existing in the municipal capital of Coquimatlán, as
well as the characteristics that each one currently
has. The purpose of this project is to generate and
update the information that the entity has regarding
public lighting.
Keywords: Coordinates-Map-Lamps-G.P.S.
Introducción.
En este proyecto atenderemos la problemática
de actualizar la información que se tiene en el
municipio de Coquimatlán, Colima. Respecto a
los dispositivos de iluminación pública.
Se utilizaron diferentes herramientas tanto para
la extracción de información como para su
procesamiento.
-Geospatial Data Abstraction Library: Por
medio de esta libreria es posible la lectura y
escritura de formatos de datos geoespaciales
publicada bajo la MIT License por la Fundación
OSGeo. Con esta librería se pueden realizar
multitud de operaciones de transformación y
procesamiento sobre gran variedad de datos
ráster y vectoriales.
-etrex® 10: Dispositivo de bolsillo que permite
saber la posición geográfica longitud y latitud
con una posición de unos metros, usando la
tecnología GPS 1. ​ Son el sustituto de los
mapas de bolsillo

-Librería Folium: Proporciona una creciente
gama de capacidades a través de sus funciones
básicas y complementos. Puede visualizar,
gestionar, editar y analizar datos y diseñar
mapas interactivos.
Desarrollo Experimental.
Los experimentos realizados en este proyecto
fueron variados. Primero intentamos hacer el
mapeo de las coordenadas con la librería gdal
en una ortofoto de la cabecera de Coquimatlán,
pero optamos en realizar un mapa con la librería
Folium ya que consideramos que el manejo de
los datos sería más fácil y practico con esta
librería.
Para la obtención de las coordenadas de todos
los dispositivos de iluminación pública tuvimos
que utilizar un navegador G.P.S proporcionado
por el ing. César Iván Lomelí. La extracción de
los puntos la dividimos en cuatro días, del 27 al
30 del mes de septiembre del presente año.
Lo primero que intentamos con la opción de
utilizar Folium para el mapeo, fue de hacer el
mapa con el sistema de coordenadas universal
transversal de Mercator (UTM), pero esto no

2

Eduardo Barreto Campos,  Ramon Martínez Bravo//Configuración de equipo.

funcionó, ya que la librería utilizada no permite
trabajar con UTM y estas se tuvieron que
transformar al sistema de coordenadas
geográficas decimales (sistema de coordenadas
con el cual se trabaja en la librería Folium).
Ya con las coordenadas geográficas decimales
correctas, lo siguiente fue realizar el Script que
nos permitiera realizar el mapa interactivo con
todo lo deseado (tipo de luminaria, su
funcionamiento, voltaje y fecha del
levantamiento).

Script para la creación de un mapa interactivo.

Mapa interactivo obtenido.

Coordenadas Geográficas Decimales utilizadas.
Manejo de Datos.
Los datos manejados en este proyecto sólo fue el
cambio de coordenadas de un sistema a otro.

El problema al que nos enfrentamos fue a la
conversión de coordenadas UTM a Geográficas
decimales, buscamos muchas formas de hacerlo,
pero lo que nos pareció más fácil y efectivo fue un
método que involucro a tres softwares, Google
Earth, AutoCAD y Excel. Lo primero que hicimos
para este método fue exportar el archivo .csv que
contenía las coordenadas en AutoCAD para
después con el módulo CilvilCAD exportar los
puntos a Google Earth. Una vez con todos los
puntos ya en el software sólo bastó con configurar
éste para trabajar con coordenadas de tipo
Geográficas decimales, lo siguiente fue guardar el
grupo de puntos como archivo .kml esto haría la
conversión de sistemas de coordenadas. Excel nos
ayudaría a manipular el archivo .kml ya que sólo
cambiamos la extensión de este a .xml un formato
que nos permitiría la lectura y edición de las
coordenadas geográficas decimales del archivo
.kml.

Vista de la conversión del archivo .kml a .xml

Análisis de Resultados.
Los resultados obtenidos en este proyecto
fueron satisfactorios ya que cumplieron con el
objetivo.
La primera parte del proyectó que fue la
extracción de coordenadas de los dispositivos
de luminaria en Coquimatlán, Colima. se realizó
con éxito, ya que se levantó el 100% de los
dispositivos que fueron 1,109 de los cuales 31
estaban en mal estado, 32 con un
funcionamiento regular y el resto funcionando
de forma correcta. Posteriormente se comenzó
con la búsqueda y la ejecución del Script
adecuado de acuerdo con lo planeado. En este
paso nos dimos cuenta de que las coordenadas
obtenidas con el navegador no estaban en el
sistema correcto para trabajar con la librería
Folium. Esto provocó una parte más a trabajar
en el proyecto que fue la conversión de
coordenadas. Ya con las coordenadas en el
formato adecuado proseguimos con la
realización del Script. El Script cumplió en un
90% la función que se esperaba que realizara,

Vista de las Coordenadas UTM obtenidas con el
navegador G.P.S.

3

Eduardo Barreto Campos, Ramon Martínez Bravo//Configuración de equipo.

el inconveniente que no pudimos resolver en
éste fue la ejecución de unas líneas de código
que no generar ningún error pero que no
cumplen con su función que era poner
diferentes colores en los puntos generados para
diferenciar entre los dispositivos entre buen
funcionamiento, regular y malo en el mapa
interactivo. De ahí en más, todo funcionó de
forma correcta.

En la imagen podemos observar que de la línea de
código de 11 a la 14 son las que no cumplen con su
función.
Conclusiones.
Como conclusión de este proyecto es que sí se
logró el objetivo que era generar un mapa
interactivo con los puntos de ubicación de los
dispositivos de luminaria y cada uno de estos
con sus respectivas características en el
municipio de Coquimatlán, Colima. Como
observación podemos decir que se pudo haber
realizado con mayor facilidad de acuerdo con el
tema de las coordenadas con las que trabaja la
librería.
Una meta no cumplida en este proyecto fue lograr fue leer el archivo y que automáticamente lograra poner de diferentes colores las lamparas según su funcionalidad, lo que se tuvo que hacer fue poner diferentes alturas a estas para lograr poner diferentes colores.
Bibliografía.


https://www.youtube.com/watch?v=Ftcz
p3bx1uw

https://relopezbriega.github.io/blog/2016
/09/18/visualizaciones-de-datos-con-
python/

 https://www.geofumadas.com/convertir-
coordenadas-de-google-earth-a-excel/

https://www.youtube.com/watch?v=HVxr
Byb7k8g

https://www.pybonacci.org/2017/09/07/c
omo-crear-un-mapa-interactivo-con-
folium/

4

Eduardo Barreto Campos, Ramon Martínez Bravo//Configuración de equipo.
