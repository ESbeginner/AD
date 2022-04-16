import pandas as pd #en esta primera línea estamos importando la librería, pero con un nombre más corto, así se nos hace menos pesado hacer uso de esta librería
data = pd.read_csv("Estacions_de_rec_rrega_per_a_vehicle_el_ctric_a_Catalunya.csv") #la función read_csv() sirve, pues para eso, leer archivos csv. Nótese que para hacer
                                                                                    #hacer uso de una función dentro de pandas hay que usar el formato
                                                                                    # {nombre de librería}.{nombre de la función}. Esto se debe a que las librerías no son
                                                                                    # más que un archivo de python con un <<objeto>>, y este a su vez tiene funciones
                                                                                    # definidas dentro de sí
df=pd.DataFrame(data) #Lo que hacemos con esta función es cojer el archivo csv, ahora conocido como <<data>>  organizarlo siguiendo un patrón tipo matriz MxN
accesos = df["ACCES"]
provincia = df["PROVINCIA"]
municipi = df["MUNICIPI"]
nplazas = df["NPLACES ESTACIÓ"]
AD1 = pd.DataFrame([accesos,provincia,municipi,nplazas]).T #
AD2 = AD1.dropna()

AD3 = AD2.reset_index()

if __name__ == "__main__": # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True
  print(AD3) # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
Todas las combinaciones de NPLACES son
https://aprendeconalf.es/docencia/python/manual/pandas/

'''
