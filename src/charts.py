import matplotlib.pyplot as plt
import os

class GeneradorGraficos: # <--- REVISA QUE ESTÉ ESCRITO EXACTAMENTE ASÍ
    def __init__(self, output_dir="reports/"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # Configuración estética
        plt.style.use('ggplot')

    def generar_reporte_visual(self, resultados):
        # 1. Gráfico de barras: Ventas sin IGV por sede
        plt.figure(figsize=(10, 6))
        resultados['por_sede'].plot(kind='bar', color='skyblue')
        plt.title('Ventas sin IGV por Sede')
        plt.xlabel('Sede')
        plt.ylabel('Monto ($)')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}ventas_sede.png")
        plt.close()

        # 2. Gráfico de barras horizontales: Top 5 modelos
        plt.figure(figsize=(10, 6))
        resultados['top_5'].sort_values().plot(kind='barh', color='salmon')
        plt.title('Top 5 Modelos más Vendidos')
        plt.xlabel('Cantidad de Ventas')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}top_modelos.png")
        plt.close()

        # 3. Gráfico de barras: Canales con más ventas
        plt.figure(figsize=(10, 6))
        resultados['canales'].plot(kind='bar', color='lightgreen')
        plt.title('Ventas por Canal de Comunicación')
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}canales_ventas.png")
        plt.close()

        # 4. Gráfico circular: Segmento de clientes
        plt.figure(figsize=(8, 8))
        resultados['segmentos'].plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Segmentación de Clientes por Monto')
        plt.ylabel('') 
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}segmento_clientes.png")
        plt.close()

        print(f"🖼️ Gráficos generados exitosamente en: {self.output_dir}")