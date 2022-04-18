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
NPBarcelona = []
NPTarragona = []
NPLleida = []
NPGirona = []

NPMBarcelona = []
NPMBadalona = []
NPMManresa = []
NPMMataro = []
NPMSant_Pere_de_Ribes = []
NPMSitges = []
NPMGAva = []
NPMGranollers = []
NPMLHospitalet_de_Llobregat = []
NPMLa_Roca_del_Valles = []
NPMSant_Cugat_del_Valles = [] #OSant_Cubat_del_Valles
NPMTerrassa = []
NPMBarberà_del_Valles = []
NPMCabrera_de_Mar = []
NPMCastelldefels = []
NPMEl_Masnou = []
NPMSabadell = []
NPMSubirats = []
NPMVic = []
NPMAlella = []
NPMBerga = []
NPMConrellà_de_Llobregat = [] #CORNELLÀ DE LLOBREGAT
NPMCabrils = []
NPMCaldes_dEstrach = []
NPMCaldes_de_Montbui = []
NPMCanet_de_Mar = []
NPMCardona = []
NPMEl_Prat_de_Llobregat = [] #EL PRAT DE LLOBREGAT
NPMEsparraguera = []
NPMIgualada = []
NPMLa_Garriga = []
NPMLlinars_del_Valles = []
NPMLloret_de_Mar = []
NPMMartorell = [] #MARTORELL
NPMMontcada_i_Reixac = []
NPMMontmelo = []
NPMMontornés_del_Valles = []
NPMPachs_del_Penedes = []
NPMPalleja = []
NPMPineda_de_Mar = []
NPMSant_Quirze_del_Valles = []
NPMSant_Adria_del_Besos = []
NPMSant_Fruitos_de_Bages = []
NPMSant_Joan_Despi = []
NPMSant_Pere_Vilamajor = []
NPMSanta_Coloma_de_Gramenet = []
NPMSantpedor = []
NPMTona = []
NPMVAllromanes = []
NPMViladecans = []
NPMVilafranca_del_Penedes = []
NPMVilanova_i_la_Geltru = []
NPMÀvia = []
NPMOtro = []

for i in range(len(provincia)):
    if provincia[i] == "Barcelona":
        if municipi[i] == "Barcelona":
            NPMBarcelona.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Badalona":
            NPMBadalona.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Manresa":
            NPMManresa.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Mataró":
            NPMMataro.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Pere de Ribes":
            NPMSant_Pere_de_Ribes.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sitges":
            NPMSitges.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Gavà":
            NPMGAva.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Granollers":
            NPMGranollers.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "L'Hospitalet de Llobregat":
            NPMLHospitalet_de_Llobregat.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "La Roca del Vallès":
            NPMLa_Roca_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Cugat del Vallès" or municipi[i] == "Sant Cugat del Valles":
            NPMSant_Cugat_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Terrassa":
            NPMTerrassa .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Barberà del Vallès":
            NPMBarberà_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Cabrera de Mar":
            NPMCabrera_de_Mar.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Castelldefels":
            NPMCastelldefels .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "El Masnou":
            NPMEl_Masnou.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sabadell":
            NPMSabadell.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Subirats":
            NPMSubirats.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Vic":
            NPMVic.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Alella":
            NPMAlella .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Berga":
            NPMBerga .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Cornellà del Llobregat" or municipi[i] == "CORNELLÀ DEL LLOBREGAT":
            NPMConrellà_de_Llobregat.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Cabrils":
            NPMCabrils.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Caldes d'Estrach":
            NPMCaldes_dEstrach.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Caldes de Montbui":
            NPMCaldes_de_Montbui.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Canet de Mar":
            NPMCanet_de_Mar.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Cardona":
            NPMCardona .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "El Prat de Llobregat" or municipi[i] == "EL PRAT DE LLOBREGAT":
            NPMEl_Prat_de_Llobregat.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Esparraguera":
            NPMEsparraguera .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Igualada":
            NPMIgualada .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "La Garriga":
            NPMLa_Garriga.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Llinars del Vallès":
            NPMLlinars_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Lloret de Mar":
            NPMLloret_de_Mar.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Martorell" or municipi[i] == "MARTORELL":
            NPMMartorell .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Montcada i Reixac":
            NPMMontcada_i_Reixac.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Montmeló":
            NPMMontmelo.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Montmeló":
            NPMMontornés_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Pachs del Penedés":
            NPMPachs_del_Panedes.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Pallejà":
            NPMPalleja .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Pineda de Mar":
            NPMPineda_de_Mar.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Quirze del Vallès":
            NPMSant_Quirze_del_Valles.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Adrià del Besòs":
            NPMSant_Adria_del_Besos.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Fruitós de Bages":
            NPMSant_Fruitos_de_Bages.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Joan Despí":
            NPMSant_Joan_Despi.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Sant Pere Vilamajor":
            NPMSant_Pere_Vilamajor.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Santa Coloma de Gramenet":
            NPMSanta_Coloma_de_Gramenet.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Santpedor":
            NPMSantpedor .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Tona":
            NPMTona .append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Vallromanes":
            NPMVAllromanes.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Viladecans":
            NPMViladecans.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Vilafranca del Penedés":
            NPMVilafranca_del_Penedes.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        elif municipi[i] == "Vilanova i la Geltrú":
            NPMVilanova_i_la_Geltru.append(nplazas[i])
            NPBarcelona.append(nplazas[i])

        else:
            NPMOtro.append(nplazas[i])
            NPBarcelona.append(nplazas[i])


    elif provincia[i] == "Tarragona":
        NPTarragona.append(nplazas[i])

    elif provincia[i] == "Lleida":
        NPLleida.append(nplazas[i])

    elif provincia[i] == "Girona":
        NPGirona.append(nplazas[i])

NPbarcelona = sum(NPBarcelona)
NPTarragona = sum(NPTarragona)
NPLlleida = sum(NPLleida)
NPGirona = sum(NPGirona)
NPMBarcelona = sum(NPMBarcelona)
NPMBadalona = sum(NPMBadalona)
NPMManresa =sum(NPMManresa)
NPMMataro  = sum(NPMMataro)
NPMSant_Pere_de_Ribes = sum(NPMSant_Pere_de_Ribes)
NPMSitges =sum(NPMSitges)
NPMGAva =sum(NPMGAva)
NPMGranollers = sum(NPMGranollers)
NPMLHospitalet_de_Llobregat = sum(NPMLHospitalet_de_Llobregat)
NPMLa_Roca_del_Valles = sum(NPMLa_Roca_del_Valles)
NPMSant_Cugat_del_Valles = sum(NPMSant_Cugat_del_Valles)
NPMTerrassa = sum(NPMTerrassa)
NPMBarberà_del_Valles = sum(NPMBarberà_del_Valles)
NPMCabrera_de_Mar = sum(NPMCabrera_de_Mar)
NPMCastelldefels = sum(NPMCastelldefels)
NPMEl_Masnou = sum(NPMEl_Masnou)
NPMSabadell =sum(NPMSabadell)
NPMSubirats = sum(NPMSubirats)
NPMVic = sum(NPMVic)
NPMAlella = sum(NPMAlella)
NPMBerga = sum(NPMBerga)
NPMConrellà_de_Llobregat = sum(NPMConrellà_de_Llobregat)
NPMCabrils = sum(NPMCabrils)
NPMCaldes_dEstrach = sum(NPMCaldes_dEstrach)
NPMCaldes_de_Montbui = sum(NPMCaldes_de_Montbui)
NPMCanet_de_Mar = sum(NPMCanet_de_Mar)
NPMCardona = sum(NPMCardona)
NPMEl_Prat_de_Llobregat = sum(NPMEl_Prat_de_Llobregat)
NPMEsparraguera = sum(NPMEsparraguera)
NPMIgualada = sum(NPMIgualada)
NPMLa_Garriga = sum(NPMLa_Garriga)
NPMLlinars_del_Valles = sum(NPMLlinars_del_Valles)
NPMLloret_de_Mar = sum(NPMLloret_de_Mar)
NPMMartorell = sum(NPMMartorell)
NPMMontcada_i_Reixac = sum(NPMMontcada_i_Reixac)
NPMMontmelo = sum(NPMMontmelo)
NPMMontornés_del_Valles = sum(NPMMontornés_del_Valles)
NPMPachs_del_Penedes = sum(NPMPachs_del_Penedes)
NPMPalleja = sum(NPMPalleja)
NPMPineda_de_Mar = sum(NPMPineda_de_Mar)
NPMSant_Quirze_del_Valles = sum(NPMSant_Quirze_del_Valles)
NPMSant_Adria_del_Besos = sum(NPMSant_Adria_del_Besos)
NPMSant_Fruitos_de_Bages = sum(NPMSant_Fruitos_de_Bages)
NPMSant_Joan_Despi = sum(NPMSant_Joan_Despi)
NPMSant_Pere_Vilamajor = sum(NPMSant_Pere_Vilamajor)
NPMSanta_Coloma_de_Gramenet = sum(NPMSanta_Coloma_de_Gramenet)
NPMSantpedor = sum(NPMSantpedor)
NPMTona = sum(NPMTona)
NPMVAllromanes = sum(NPMVAllromanes)
NPMViladecans = sum(NPMViladecans)
NPMVilafranca_del_Penedes = sum(NPMVilafranca_del_Penedes)
NPMVilanova_i_la_Geltru = sum(NPMVilanova_i_la_Geltru)
NPMÀvia = sum(NPMÀvia)

#Quesito municipios de Barcelona

#Quesito municipios de Tarragona
#Quesito municipios de Lleida
#Quesito municipios de Girona

#Primer quesito grande de accesos
'''
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
'''
#Primer quesito grande de municipios

################################################################################

#Segunda parte; gráficos
'''
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

plt.show()
'''
################################################################################
#Test Sunchart
'''
import plotly.graph_objects as go
NPP = [NPbarcelona, NPTarragona, NPLlleida, NPGirona]
NP = ['Barcelona', 'Tarragona', 'Lleida', 'Girona']
fig1 = go.Figure(go.Sunburst(
    labels = NP,
    values = [NPbarcelona, NPTarragona, NPLlleida, NPGirona]
))

fig1.update_traces(textinfo="label+percent parent",level=5, selector=dict(type="sunburst"))
fig1.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig2 = go.Figure(go.Sunburst(
    labels = ['Barcelona','Badalona','Manresa','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4'],
    values = [NPMBarcelona,NPMBadalona,NPMManresa,NPMMataro,NPMSant_Pere_de_Ribes,NPMSitges,NPMGAva,NPMGranollers,NPMLHospitalet_de_Llobregat,NPMLa_Roca_del_Valles,NPMSant_Cugat_del_Valles,NPMTerrassa,NPMBarberà_del_Valles,NPMCabrera_de_Mar,NPMCastelldefels,NPMEl_Masnou,NPMSabadell,NPMSubirats,NPMVic,NPMAlella,NPMBerga,NPMConrellà_de_Llobregat,NPMCabrils,NPMCaldes_dEstrach,NPMCaldes_de_Montbui,
    NPMCanet_de_Mar,NPMCardona,NPMEl_Prat_de_Llobregat,NPMEsparraguera,NPMIgualada,NPMLa_Garriga,NPMLlinars_del_Valles,NPMLloret_de_Mar,NPMMartorell,
    NPMMontcada_i_Reixac,NPMMontmelo,NPMMontornés_del_Valles,NPMPachs_del_Penedes,NPMPalleja,NPMPineda_de_Mar,NPMSant_Quirze_del_Valles,NPMSant_Adria_del_Besos,NPMSant_Fruitos_de_Bages,NPMSant_Joan_Despi,NPMSant_Pere_Vilamajor,NPMSanta_Coloma_de_Gramenet,NPMSantpedor,NPMTona,NPMVAllromanes,NPMViladecans,NPMVilafranca_del_Penedes,NPMVilanova_i_la_Geltru,NPMÀvia,NPMOtro]
))


fig2.update_traces(textinfo="label+percent parent")
fig2.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig1.show()
fig2.show()
'''
import plotly.express as px
fig = px.sunburst(AD3,
                  path = ["PROVINCIA","MUNICIPI"],
                  values = "NPLACES ESTACIÓ",
                  title = "Funciona por favor")

fig.show()
################################################################################
#Testeo
if __name__ == "__main__": # esta sección se encarga de que si somos nosotros lo que ejecutamos el código, se active el condicionante if==True
  print(NPMMataro)
  print(NPMMontmelo)
   # Con esto podremos ver los datos. Para ver solo los 5 primeros es recomendable usar la función Head()
# PROMOTOR-GESTOR, ACCES, TIPUS VELOCITAT, TIPUS CONNEXIÓ, LATITUD, LONGITUD, DESIGNACIÓ-DESCRIPTIVA, POTENCIA, TIPUS DE CORRENT
# IDENTIFICADOR, ADREÇA, PROVINCIA, CODIPROV, MUNICIPI, NPLACES ESTACIÓ, TIPUS VEHICLE, Columna amb georeferència POINT.

'''
ACCES(público, privado), PROVINCIA, MUNICIPI, NPLACES ESTACIÓ
Todas las combinaciones de NPLACES son
https://aprendeconalf.es/docencia/python/manual/pandas/

'''
