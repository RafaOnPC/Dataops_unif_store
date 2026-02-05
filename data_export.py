import os
import pandas as pd


def extraer_mes(nombre_archivo):
    # Extraccion del mes
    nombre = os.path.splitext(nombre_archivo)[0]
    partes = nombre.split('_')
    mes = partes[-1]
    return mes.title()


def exportar_datos(df):
    # Crear carpeta output si no existe
    os.makedirs('output', exist_ok=True)

    archivo_global = os.path.join('output', 'Fich_Ventas_GLOBAL.xlsx')

    # Exportacion por Mes agrupacion por columna Archivo_origen
    for archivo_origen, df_mes in df.groupby('archivo_origen'):
        mes = extraer_mes(archivo_origen)

        archivo_excel = os.path.join(
            'output',
            f'Fich_Ventas_{mes}.xlsx'
        )

        df_export = df_mes.drop(columns=['archivo_origen'], errors='ignore')
        df_export.to_excel(archivo_excel, index=False)

        print(f'Archivo generado: {archivo_excel}')

    # Creacion de archivo global
    df_nuevo = df.drop(columns=['archivo_origen'], errors='ignore')

    if os.path.exists(archivo_global):
        df_global = pd.read_excel(archivo_global, dtype=str)
        df_global = pd.concat([df_global, df_nuevo], ignore_index=True)
        print('Archivo global existente actualizado')
    else:
        df_global = df_nuevo.copy()
        print('Archivo global creado')

    df_global.to_excel(archivo_global, index=False)
    print(f'Archivo global generado/actualizado: {archivo_global}')
    print('ETL finalizado correctamente')


if __name__ == "__main__":
    entrada = os.path.join('output', 'transform_output.csv')
    df = pd.read_csv(entrada, dtype=str)
    exportar_datos(df)
