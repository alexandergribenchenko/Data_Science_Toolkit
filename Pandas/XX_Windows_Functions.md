
```python
import pandas as pd
import numpy as np

# Crear matriz de ejemplo con valores aleatorios
rng = pd.date_range('20210101', periods=60, freq='D')
df = pd.DataFrame({'fecha': rng, 'valor': np.random.randint(0, 100, size=(60))})
df = df.groupby(pd.Grouper(key='fecha', freq='M')).sum().reset_index()
df = pd.concat([df]*3, ignore_index=True)
df['valor'] = np.random.randint(0, 100, size=(len(df)))
df['fecha'] = df['fecha'].dt.strftime('%Y%m')
print(df)


ventas = pd.Series([10, 5, 8, 12, 7, 9, 6, 11, 10, 8])
media_movil = ventas.rolling(window=3).mean()



dict_sample = {'fecha': ['202101', '202101', '202102', '202102', '202102', '202102', '202103', '202103', '202103', '202104', '202104', '202104', '202105', '202105', '202105', '202105', '202106', '202106'], 'valor': [5, 0, 61, 27, 26, 74, 61, 91, 27, 88, 43, 76, 2, 61, 83, 96, 29, 69]}
dict_sample


# Calcular la mediana de los valores agregados de los 3 meses anteriores para cada uno de los meses
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y%m')
df = df.sort_values(by='fecha')
df['mediana'] = df.groupby(df['fecha'].dt.strftime('%Y%m'))['valor'].transform('median')
df['valor_3_meses_antes'] = df['valor'].shift(3)
df = df[df['fecha'] >= df['fecha'].min() + pd.DateOffset(months=3)]
print(df)




rt_value = 'BOGSCL'
airline_code_value = 'LA'
porcentaje = 0.25
cantidad_meses_hacia_atras = 3

lista_aerolinea = []

asks_mediana = []
asks_mediana_umbral_superior = []
asks_mediana_umbral_inferior = []

for index,date in enumerate(dates_all):
 
  mes_interes = date
  meses_previos = dates_all[index+1:index+1+cantidad_meses_hacia_atras]
  
  asks_mediana_value = df.sum_asks[(df.airline_code==airline_code_value)&
                           (df.rt==rt_value)&
                           (df.flight_date.isin(meses_previos))].median()
  
#   asks_mediana_umbral_superior = (1+porcentaje)*asks_mediana
#   asks_mediana_umbral_inferior = (1-porcentaje)*asks_mediana
  
#   print(index, mes_interes, meses_previos, asks_mediana, asks_mediana_umbral_superior, asks_mediana_umbral_inferior)
  asks_mediana += [asks_mediana_value]
  asks_mediana_umbral_superior += [(1+porcentaje)*asks_mediana_value]
  asks_mediana_umbral_inferior += [(1-porcentaje)*asks_mediana_value]



```
