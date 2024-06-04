import pandas as pd

csv_filename = f'CostoxAccidenteT1.csv'
df = pd.read_csv(csv_filename)

years = df.iloc[1:, 0]
print(years)

dataT1 = df.iloc[1:, 1:3]
costoT1 = df.iloc[1:, 1]
frecuenciaT1 = df.iloc[1:, 2]
print(costoT1)
print(frecuenciaT1)

dataT2 = df.iloc[1:, 3:5]
costoT2 = df.iloc[1:, 3]
frecuenciaT2 = df.iloc[1:, 4]
print(costoT2)
print(frecuenciaT2)

dataT3 = df.iloc[1:, 5:]
costoT3 = df.iloc[1:, 5]
frecuenciaT3 = df.iloc[1:, 6]
print(costoT3)
print(frecuenciaT3)

print(years.get(1))
print(costoT1.get(1))
print(frecuenciaT1.get(1))
print(costoT2.get(1))
print(frecuenciaT2.get(1))
print(costoT3.get(1))
print(frecuenciaT3.get(1))
