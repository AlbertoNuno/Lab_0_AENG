import Funciones as fn
import Visualizaciones as vs
import pandas as pd
from Datos import token
import numpy as np
import string as str

#asia = np.array([])


#token = '40a4858c00646a218d055374c2950239-f520f4a80719d9749cc020ddb5188887'
instrumento = "EUR_USD"
granularidad = "D"

f_inicio = pd.to_datetime("2019-01-06 00:00:00").tz_localize('GMT')
f_fin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')

df_pe= fn.f_precios_masivos(p0_fini=f_inicio, p1_ffin=f_fin, p2_gran=granularidad,
                            p3_inst=instrumento, p4_oatk=token, p5_ginc=4900)

vs_grafica1=vs.g_velas(p0_de=df_pe.iloc[0:120,:])
#vs_grafica1.show()

pip_mult = 1000

df_pe['Hora']= list(df_pe['TimeStamp'][i].hour for i in range(0,len(df_pe['TimeStamp'])))#nueva columna de hora
df_pe['Dia']=list(df_pe['TimeStamp'][i].weekday() for i in range(0, len(df_pe['TimeStamp'])))
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


high = pd.DataFrame(float(i) for i in df_pe['High'])
low = pd.DataFrame(float(i) for i in df_pe['Low'])
df_pe['hl']=(high-low)*10000
direccion = lambda open,close : 'Alcista' if close>=open else 'Bajista'

df_pe['sentido']=pd.DataFrame( direccion(df_pe['Open'][i],df_pe['Close'][i]) for i in range(len(df_pe['Open'])))






#for i in range(len(sesiones)):
 #   for j in range(len(sesiones[i])): ## iteracion sobre el arreglo elegido
  #      if(df_pe['Hora'][]








#df_pe['Close-open']=(float(df_pe['Close'])-float(df_pe['Open'])) *pip_mult## box plot de amplitud de velas (close - open),
# se multiplica por el 10000 para expresar el resultado en pips


