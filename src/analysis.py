import pandas as pd

class AnalizadorVentas:
    def __init__(self, ruta_excel):
        self.ruta = ruta_excel

    def realizar_calculos(self):
        try:
            # 1. Carga de hojas
            df_ventas = pd.read_excel(self.ruta, sheet_name='VENTAS')
            df_vehiculos = pd.read_excel(self.ruta, sheet_name='VEHICULOS')
        except Exception as e:
            raise Exception(f"Error al leer las hojas del Excel: {str(e)}")

        # 2. Limpieza de nombres de columnas (quitar espacios y poner _)
        df_ventas.columns = [c.strip().replace(' ', '_') for c in df_ventas.columns]
        df_vehiculos.columns = [c.strip().replace(' ', '_') for c in df_vehiculos.columns]

        # 3. Estandarización de la llave de unión (QUITAR TILDES)
        # Forzamos que en ambas tablas se llame 'ID_Vehiculo'
        df_ventas = df_ventas.rename(columns={'ID_Vehículo': 'ID_Vehiculo'})
        df_vehiculos = df_vehiculos.rename(columns={'ID_Vehículo': 'ID_Vehiculo'})

        # 4. UNIÓN DE TABLAS (Merge)
        df = pd.merge(df_ventas, df_vehiculos, on='ID_Vehiculo', how='left')

        # 5. Mapeo de columnas según tu archivo real
        col_venta = 'Precio_Venta_sin_IGV'
        col_igv = 'Precio_Venta_Real'
        col_canal = 'Canal'
        col_sede = 'Sede'
        col_modelo = 'MODELO'

        # 6. Retorno de resultados (Incluyendo 'canales' para evitar el error crítico)
        return {
            'total_ventas': len(df),
            'total_sin_igv': df[col_venta].sum(),
            'total_con_igv': df[col_igv].sum(),
            'por_sede': df.groupby(col_sede)[col_venta].sum(),
            'top_5': df[col_modelo].value_counts().head(5),
            'canales': df[col_canal].value_counts(), # <--- Solución al error 'canales'
            'datos_completos': df
        }