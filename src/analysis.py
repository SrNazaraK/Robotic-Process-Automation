import pandas as pd

class AnalizadorVentas:
    def __init__(self, path):
        self.df = pd.read_excel(path)
        # Asumiendo que el IGV en Venezuela es 16% (0.16)
        # Si tu Excel ya tiene las columnas, solo las procesamos
        
    def realizar_calculos(self):
        # 8 y 9. Conteos básicos
        total_ventas_cant = len(self.df)
        clientes_unicos = self.df['Cliente'].nunique()
        
        # 4. Ventas sin IGV por sede
        ventas_sede = self.df.groupby('Sede')['Venta_sin_IGV'].sum()
        
        # 5. Top 5 modelos
        top_modelos = self.df['Modelo'].value_counts().head(5)
        
        # 10. Totales Generales
        total_sin_igv = self.df['Venta_sin_IGV'].sum()
        total_con_igv = self.df['Venta_con_IGV'].sum()
        
        return {
            "total_ventas": total_ventas_cant,
            "clientes": clientes_unicos,
            "por_sede": ventas_sede,
            "top_5": top_modelos,
            "total_sin": total_sin_igv,
            "total_con": total_con_igv
        }