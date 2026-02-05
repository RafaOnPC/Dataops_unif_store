import pandas as pd
import os

def transformar_datos(df):
    # Commit #1 

    # 1. ELIMINAR DUPLICADOS
    df = df.drop_duplicates()

    # Asegurar que stock y vendidos sean numéricos
    df['stock'] = pd.to_numeric(df['stock'], errors='coerce').fillna(0)
    df['vendidos'] = pd.to_numeric(df['vendidos'], errors='coerce').fillna(0)

    # 2. VERIFICAR QUE VENDIDOS <= STOCK
    df.loc[df['vendidos'] > df['stock'], 'vendidos'] = df['stock']

    # 3. APLICAR TITLE CASE
    columnas_texto = ['producto', 'marca', 'categoria']
    for col in columnas_texto:
        df[col] = df[col].str.title()

    return df

if __name__ == "__main__":
    entrada = os.path.join('output', 'read_output.csv')
    salida = os.path.join('output', 'transform_output.csv')

    df = pd.read_csv(entrada, dtype=str)
    df = transformar_datos(df)

    df.to_csv(salida, index=False)
    print(f'Datos TRANSFORM guardados en: {salida}')
