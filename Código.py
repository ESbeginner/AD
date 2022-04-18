#Primera parte; filtrado de datos
#Primeramente cargamos todas las librerias necesarias y les asignamos un nombre
#más comodo para que sea más fácil llamarlas en el futuro
#Es importante tener las librerias instaladas para un correcto funcionamiento
#Para instalar una libreria en el dispositivo utilitzar en la consola el comando
#pip install "nombre_de_la_libreria"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Empezamos leyendo la base de datos con la que trabajaremos
data = pd.read_csv("Estacions_de_rec_rrega_per_a_vehicle_el_ctric_a_Catalunya.csv")
df=pd.DataFrame(data) #Definimos toda la base de datos con el nombre df

#Seleccionamos las columnas que nos interesan y les damos un nombre
accesos = df["ACCES"]
provincia = df["PROVINCIA"]
municipi = df["MUNICIPI"]
nplazas = df["NPLACES ESTACIÓ"]

#Creamos una nueva lista con los datos que nos interesan
AD1 = pd.DataFrame([accesos,provincia,municipi,nplazas]).T
AD2 = AD1.dropna() #Eliminamos las filas con algun valor nulo

AD3 = AD2.reset_index(drop=True) #Al haber eliminado filas la numeración de filas
                                 #se ha estropeado, con esto reiniciamos el índice

#Quitaremos aquellos valores valores con los que no podemos trabajar (Ej. 3+2)
temp = [] #comenzamos creando una lista vacia
for i in AD3["NPLACES ESTACIÓ"]:
    try:
        #Con esto transformamos los valores que se pueden transformar en int
        AD3.loc[AD3["NPLACES ESTACIÓ"] == i, "NPLACES ESTACIÓ"] = int(i)

    except ValueError:
        #Los valores que no se pueden transformar en int se quedaran con la clase
        #str
        pass

#Añadimos de vuelta los valores con su nueva clase
for i in AD3["NPLACES ESTACIÓ"]:
    try:
        #Los valores con su clase cambiada y sin cambiar son agregados a la
        #lista temp
        temp.append(i)
    except ValueError:
        pass

nindex = []
for i in range(len(temp)):
    if type(temp[i]) == str: #Se determina el índice de todos los valores
        nindex.append(i)     #que son str

AD3 = AD3.drop(AD3.index[nindex]) #Se eliminan las filas con valores no int

AD3 = AD3.reset_index(drop=True) #Se hace de nuevo el índice

################################################################################

#Preparamos todos los datos para representar
accesos = AD3["ACCES"]
provincia = AD3["PROVINCIA"]
municipi = AD3["MUNICIPI"]
nplazas = AD3["NPLACES ESTACIÓ"]

#Primer quesito grande de provincias
Nbarcelona = []
Ntarragona = []
Nlleida = []
Ngirona = []

for i in range(len(provincia)):
    if provincia[i] == "Barcelona":
        Nbarcelona.append(nplazas[i])

    elif provincia[i] == "Tarragona":
        Ntarragona.append(nplazas[i])

    elif provincia[i] == "Lleida":
        Nlleida.append(nplazas[i])

    elif provincia[i] == "Girona":
        Ngirona.append(nplazas[i])


Nbarcelona = sum(Nbarcelona)
Ntarragona = sum(Ntarragona)
Nlleida = sum(Nlleida)
Ngirona = sum(Ngirona)

#Primer quesito grande de accesos
NCC = []
NHOTEL = []
NPUBLIC = []
NVIA_PUBLICA = []
NSERVEI = []
NPRIVAT = []
NALTRES = []

for i in range(len(accesos)):
    if accesos[i] == "APARCAMENT CC":
        NCC.append(nplazas[i])

    elif accesos[i] == "HOTEL" or accesos[i] == "APARCAMENT HOTEL" :
        NHOTEL.append(nplazas[i])

    elif accesos[i] == "APARCAMENT PUBLIC" or accesos[i] == "APARCAMENT PÚBLIC":
        NPUBLIC.append(nplazas[i])

    elif accesos[i] == "VIA PUBLICA" or accesos[i] == "VIA PÚBLICA":
        NVIA_PUBLICA.append(nplazas[i])

    elif accesos[i] == "ESTACIÓ SERVEI" or accesos[i] == "ESTACIÓ DE SERVEI":
        NSERVEI.append(nplazas[i])

    else:
        NALTRES.append(nplazas[i])

NCC = sum(NCC)
NHOTEL = sum(NHOTEL)
NPUBLIC = sum(NPUBLIC)
NVIA_PUBLICA = sum(NVIA_PUBLICA)
NSERVEI = sum(NSERVEI)
NALTRES = sum(NALTRES)

#Primer quesito grande de municipios

################################################################################

#Segunda parte; gráficos
import matplotlib.cm as cm
import matplotlib.colors as colors
plt.subplot(2, 1, 1)
PROVINCIAS = [Nbarcelona, Ntarragona, Nlleida, Ngirona]
Nombres = ["Barcelona", "Tarragona", "Lleida", "Girona"]
Colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
desfase = (0.1, 0.1, 0.1, 0.1)
plt.pie(PROVINCIAS, labels = Nombres, autopct = "%0.1f %%", colors = Colores, explode = desfase, shadow = True)
plt.grid(True)

plt.subplot(2, 1, 2)
APARCAMENTS = [NCC, NHOTEL, NPUBLIC, NVIA_PUBLICA, NSERVEI, NALTRES]
Nombres_APARCAMIENTOS = ["Aparcament CC", "Aparcament hotel", "Aparcament públic", "Aparcament via pública", "Estació de servei", "Altres aparcaments"]
desfase = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(APARCAMENTS, labels = Nombres_APARCAMIENTOS, autopct = "%0.1f %%", explode = desfase, shadow = True)
plt.grid(True)

#plt.show()
################################################################################
#Test Sunchart
import plotly.express as px
fig1 = px.sunburst(
    data_frame=AD3,
    path = ["ACCES", "PROVINCIA", "MUNICIPI"],

)
fig1.update_traces(textinfo="label+percent parent",level=5, selector=dict(type="sunburst"))
fig1.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig2 = px.sunburst(
    data_frame=AD3,
    path = ["PROVINCIA", "MUNICIPI"],

)
fig2.update_traces(textinfo="label+percent parent")
fig2.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig1.show(), fig2.show()
################################################################################
#Testeo
if __name__ == "__main__": # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True
  print(AD3)
  print(NCC)
   # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
Todas las combinaciones de NPLACES son
https://aprendeconalf.es/docencia/python/manual/pandas/

'''
