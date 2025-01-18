import os
import pandas as pd

# Lista de archivos CSV
csv_files = [
    "./weather_data/weather01.txt",
    "./weather_data/weather02.txt",
    "./weather_data/weather03.txt",
    "./weather_data/weather04.txt",
    "./weather_data/weather05.txt",
    "./weather_data/weather06.txt",
]

# Verificar la existencia de los archivos
dataframes = []
for file in csv_files:
    if not os.path.isfile(file):
        print(f"El archivo {file} no existe.")
        continue

    # Leer cada archivo, asumiendo que están separados por espacios
    df = pd.read_csv(file, sep='\s+')
    dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Mostrar el DataFrame combinado
    print(combined_df)
else:
    print("No se encontraron archivos para combinar.")