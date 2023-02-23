
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
```
