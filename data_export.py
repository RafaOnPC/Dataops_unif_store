import os
import pandas as pd


def exportar_datos(df):
    # Crear carpeta output si no existe
    os.makedirs('output', exist_ok=True)

    archivo_global = os.path.join('output', 'Fich_Ventas_GLOBAL.xlsx')

    # Exportacion de archivos por mes
    for mes, df_mes in df.groupby('mes'):
        mes_archivo = mes.capitalize()
        archivo_excel = os.path.join(
            'output',
            f'Fich_Ventas_{mes_archivo}.xlsx'
        )

        # Eliminanacio de columna tecnica
        df_export = df_mes.drop(columns=['archivo_origen'], errors='ignore')

        df_export.to_excel(archivo_excel, index=False)
        print(f'Archivo generado: {archivo_excel}')

    # 2. Archivo global historico
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
