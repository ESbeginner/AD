#Primera parte; filtrado de datos
#Primeramente cargamos todas las librerias necesarias y les asignamos un nombre
#más comodo para que sea más fácil llamarlas en el futuro
#Es importante tener las librerias instaladas para un correcto funcionamiento
#Para instalar una libreria en el dispositivo utilitzar en la consola el comando
#pip install "nombre_de_la_libreria"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Empezamos leyendo la base de datos con la que trabajaremos
data = pd.read_csv("Estacions_de_rec_rrega_per_a_vehicle_el_ctric_a_Catalunya.csv")
df=pd.DataFrame(data) #Definimos toda la base de datos con el nombre df

#Seleccionamos las columnas que nos interasan y les damos un nombre
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

#Añadimos de vulta los valores con su nueva clase
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
'''
import matplotlib.cm as cm
import matplotlib.colors as colors

desfase = (0.1, 0.1, 0.1, 0.1)
plt.pie(AD3['NPLACES ESTACIÓ'], labels=AD3['PROVINCIA'])
plt.show()
'''
################################################################################
#Testeo
if __name__ == "__main__": # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True
  print(AD3)
   # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
Todas las combinaciones de NPLACES son
https://aprendeconalf.es/docencia/python/manual/pandas/

'''
