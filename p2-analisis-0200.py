import pandas as pd
import numpy as np
#transacciones
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}

df=pd.DataFrame(transacciones)
print(df)
print("<3<3<3<3<3<3 Agrupar por una sola columna  <3<3<3<3<3")
agrupado = df.groupby('Monto')
print(agrupado)
print(" <3<<3<3<3<3<3<3< por agrecacion <3<3<3<3<3<3<3<3<3 ")

# Salario promedio por monto
print(agrupado['Ubicacion_Inusual'].mean())
print("<3<3<3<3<3<3<3<3 Monto Maxima <3<3<3<3<3<3<3<3<3<3<3")
# Edad maxima en cada monto
print(agrupado['Es_Fraude'].max()) 
