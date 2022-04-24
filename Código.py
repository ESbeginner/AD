#Primera parte; filtrado de datos
#Primeramente cargamos todas las librerias necesarias y les asignamos un nombre
#más comodo para que sea más fácil llamarlas en el futuro
#Es importante tener las librerias instaladas para un correcto funcionamiento
#Para instalar una libreria en el dispositivo utilitzar en la consola el comando
#pip install "nombre_de_la_libreria"
import pandas as pd
import numpy as np
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
#Segunda parte; gráficos

import plotly.express as px
from plotly.subplots import make_subplots
fig1 = px.sunburst(AD3,
                  path = ["PROVINCIA","MUNICIPI","ACCES"],
                  values = "NPLACES ESTACIÓ")

fig1.update_traces(textinfo="label+percent parent+value")


fig2 = px.sunburst(AD3,
                    path = ["PROVINCIA","ACCES","MUNICIPI"],
                    values = "NPLACES ESTACIÓ")

fig2.update_traces(textinfo="label+percent parent+value")

fig3 = px.sunburst(AD3,
                  path = ["ACCES","PROVINCIA","MUNICIPI"],
                  values = "NPLACES ESTACIÓ")

fig3.update_traces(textinfo="label+percent parent+value")

fig = make_subplots(
horizontal_spacing=0.02,
vertical_spacing=0,
subplot_titles=["PROVINCIA -> ACCES -> MUNICIPI","PROVINCIA -> MUNICIPI -> ACCES","ACCES -> PROVINCIA -> MUNICIPI"],
rows=1,
cols=3,
specs=[[{"type": "sunburst"},{"type": "sunburst"}, {"type": "sunburst"}]])


fig.add_trace(fig1.data[0], row=1, col=2)
fig.add_trace(fig2.data[0], row=1, col=1)
fig.add_trace(fig3.data[0], row=1, col=3)

fig.update_layout(margin=dict(t=30, b=10, r=10, l=10))
fig.show()


################################################################################
#Testeo
 # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True

   # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
#ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
#Todas las combinaciones de NPLACES son
#https://www.delftstack.com/es/howto/python/sum-of-list-of-numbers-in-python/
#https://es.stackoverflow.com/questions/142506/regenerar-indices-en-un-pandas-dataframe-tras-eliminar-filas
#https://www.delftstack.com/es/howto/python-pandas/how-to-get-a-value-from-a-cell-of-a-dataframe/
#https://www.delftstack.com/es/howto/python-pandas/drop-row-pandas/
#https://aprendeconalf.es/docencia/python/manual/pandas/
#https://stackoverflow.com/questions/64377918/plotly-how-to-generate-side-by-side-px-sunburst-plots
#https://coderzcolumn.com/tutorials/data-science/how-to-create-sunburst-chart-in-python-plotly
'''
