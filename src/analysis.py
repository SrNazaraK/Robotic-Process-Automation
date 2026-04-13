import pandas as pd

class AnalizadorVentas:
    def __init__(self, path):
        """
        Inicializa el analizador con la ruta del archivo Excel.
        """
        self.path = path
        self.df = None

    def realizar_calculos(self):
        """
        Carga los datos y realiza los cálculos financieros y estadísticos.
        """
        # Cargar el Excel
        self.df = pd.read_excel(self.path)
        
        # --- CÁLCULOS OBLIGATORIOS ---
        
        # 8 y 9. Conteos básicos
        total_ventas_cant = len(self.df)
        clientes_unicos = self.df['Cliente'].nunique()
        
        # 4. Precio de ventas sin IGV por sede
        ventas_sede = self.df.groupby('Sede')['Venta_sin_IGV'].sum()
        
        # 5. Modelos de vehículos más vendidos (top 5)
        top_modelos = self.df['Modelo'].value_counts().head(5)
        
        # 6. Canales con más ventas
        canales_ventas = self.df['Canal'].value_counts()
        
        # 10. Totales Generales (Sumas globales)
        total_sin_igv = self.df['Venta_sin_IGV'].sum()
        total_con_igv = self.df['Venta_con_IGV'].sum()
        
        # 7. Segmento de clientes por precio (Ejemplo simple de segmentación)
        # Esto servirá para el gráfico circular más adelante
        def segmentar(monto):
            if monto > 18000: return 'Premium'
            if monto > 14000: return 'Estándar'
            return 'Económico'
        
        self.df['Segmento'] = self.df['Venta_sin_IGV'].apply(segmentar)
        segmentos = self.df['Segmento'].value_counts()

        # Retornamos el diccionario con los nombres exactos que usa main.py
        return {
            "total_ventas": total_ventas_cant,
            "clientes": clientes_unicos,
            "por_sede": ventas_sede,
            "top_5": top_modelos,
            "canales": canales_ventas,
            "segmentos": segmentos,
            "total_sin_igv": total_sin_igv, # Nombre corregido
            "total_con_igv": total_con_igv  # Nombre corregido
        }