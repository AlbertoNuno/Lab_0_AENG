import Funciones as fn
import Visualizaciones as vs
import pandas as pd
from Datos import token
import numpy as np


instrumento = "EUR_USD"
granularidad = "D"

f_inicio = pd.to_datetime("2019-01-06 00:00:00").tz_localize('GMT')
f_fin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')

df_pe= fn.f_precios_masivos(p0_fini=f_inicio, p1_ffin=f_fin, p2_gran=granularidad,
                            p3_inst=instrumento, p4_oatk=token, p5_ginc=4900)

vs_grafica1=vs.g_velas(p0_de=df_pe.iloc[0:120,:])
vs_grafica1.show()

pip_mult = 1000

df_pe['hora']= list(df_pe['TimeStamp'][i].hour for i in range(0,len(df_pe['TimeStamp'])))#nueva columna de hora
df_pe['dia']=list(df_pe['TimeStamp'][i].weekday() for i in range(0, len(df_pe['TimeStamp'])))
closes = pd.DataFrame(float(i) for i in df_pe['Close'])
open = pd.DataFrame(float(i) for i in df_pe['Open'])
df_pe['oc']=(closes-open)*10000
df_pe['mes']=pd.DataFrame(i.month for i in df_pe['TimeStamp'])

asia = np.array([22,23,0,1,2,3,4,5,6,7])
asia_europa =np.array([8])
europa = np.array([9,10,11,12])
europa_america =np.array([13,14,15,16])
america = np.array([17,18,19,20,21])
sesiones = np.array([asia,asia_europa,europa,europa_america,america])
session_names=np.array(["Asia","Asia_Europa","Europa","Europa_america","America"])

high = pd.DataFrame(float(i) for i in df_pe['High'])
low = pd.DataFrame(float(i) for i in df_pe['Low'])
df_pe['hl']=(high-low)*10000


def check_session(session_array,names,hour):
    for i in range(len(session_array)):
        for j in range(len(session_array[i])):  ## iteracion sobre el arreglo elegido
            if session_array[i][j] == hour:
                possition = i
    return names[possition]

df_pe['sesion']= pd.DataFrame(map(lambda hora:check_session(sesiones, session_names,hora), df_pe['hora']))


direccion = lambda open, close : 'Alcista' if close >= open else 'Bajista'
df_pe['sentido']=pd.DataFrame( direccion(df_pe['Open'][i],df_pe['Close'][i]) for i in range(len(df_pe['Open'])))

alcista=lambda i: 1 if i =='Alcista' else 0
df_pe['sentido_c'] = (df_pe['sentido']=='Alcista').cumsum()
df_pe['sentido_c']=(df_pe['sentido']=='Bajista').cumsum()

df_pe['volatilidad_5']= df_pe['hl'].rolling(5).max()
df_pe['volatilidad_25']=df_pe['hl'].rolling(25).max()
df_pe['Volatilidad_50']=df_pe['hl'].rolling(50).max()



