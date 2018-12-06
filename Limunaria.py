#AUTORES:
#EDUARDO PAULINO BARRETO CAMPOS
#RAMON TRINIDAD MARTINEZ BRAVO
#SE IMPORTAN LAS LIBRERIAS NECESARIAS
import folium
import pandas as pd
#CON PANDAS SE LEE EL ARCHIVO CON EXTENCION CSV EN EL QUE SE ENCUENTRAN LAS COORDENADAS 
df=pd.read_csv("Coordenadas.csv")
#CREAMOS EL MAPA CON LALIBRERIA DE FOLIUM CON LA FUNCION MAP
map=folium.Map(location=[df["LAT"].mean(),df["LON"].mean()],zoom_start=20)
#CREAMOS UN BLOQUE DONDE DEFINIREMOS LOS COLORES DE LAS LÁMPARAS DE PENDE A SUS CARACTERÍSTICAS
def color (elev):
    minimum=int(min(df['COLOR']))
    step=int((max(df['COLOR'])-min(df['COLOR']))/3)
    if elev in range(minimum,minimum+step):
        col='black'        
    elif elev in range(minimum+step,minimum+step*2):
        col='red'    
    else:
        col='red'
    return col
#NOMBRAMOS LAS CARACTERÍSTICAS DEL GRUPO CON SU RESPECTIVO NOMBRE
fg=folium.FeatureGroup(name="Localizacion de Luminarias")
#UTILIZAMOS UN CICLO PARA PODER ASIGNAR UN MARCADOR INDEPENDIENTE POR  CADA FILA DEL ARCHIVO CSV
for lat,lon,caracteristicas,elev in zip(df["LAT"],df["LON"],df["CARACTERISTICAS"],df["COLOR"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(caracteristicas)),icon=folium.Icon(color=color(elev),icon_color='black')))
map.add_child(fg)
#GUARDAMOS EL MAPA CON EXTENCION HTML
map.save(outfile="Luminarias.html")



print 'introduce el divisor de 1000/ '
d1=input()
n1=1000
dd1=float(d1)
z=n1/d1
print 'Entero',z
print 'Resto',(n1/dd1)-z


