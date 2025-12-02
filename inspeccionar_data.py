import pandas as pd

#leemos solo el primer archivo para no cargar la memoria
df = pd.read_csv('data/marketing_data_1.csv')

#mostramos la informacion clave
print("primeras 5 filas")
print(df.head())

print("\n Info del DataFrame:")
print(df.info())