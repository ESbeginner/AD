import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Estacions_de_rec_rrega_per_a_vehicle_el_ctric_a_Catalunya.csv")
df=pd.DataFrame(data)
accesos = df["ACCES"]
provincia = df["PROVINCIA"]
municipi = df["MUNICIPI"]
nplazas = df["NPLACES ESTACIÓ"]
AD1 = pd.DataFrame([accesos,provincia,municipi,nplazas]).T
AD2 = AD1.dropna()

AD3 = AD2.reset_index(drop=True)
temp = [] # lo que vamos a hacer ahora es buscar los valores de nplaces que
          # no seran trabajables posteriormente, como las sumas
for i in AD3["NPLACES ESTACIÓ"]:
    try:
        AD3.loc[AD3["NPLACES ESTACIÓ"] == i, "NPLACES ESTACIÓ"] = int(i)
    except ValueError:
        1+1
for i in AD3["NPLACES ESTACIÓ"]:
    try:
        temp.append(i)
    except ValueError:
        pass
nindex = []
for i in range(len(temp)):
    if type(temp[i]) == str:
        nindex.append(i)

AD3 = AD3.drop(AD3.index[nindex])

AD3 = AD3.reset_index(drop=True)




if __name__ == "__main__": # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True
  print(AD3) # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
  print(temp)
  print(nindex)
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
Todas las combinaciones de NPLACES son
https://aprendeconalf.es/docencia/python/manual/pandas/

'''
