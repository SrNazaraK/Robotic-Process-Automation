import matplotlib.pyplot as plt
import os

class GeneradorGraficos:
    def __init__(self, output_dir="reports/"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generar_reporte_visual(self, resultados):
        """
        Crea los gráficos PDF/PNG basados en los resultados del análisis.
        """
        # --- Gráfico 1: Ventas por Canal (Pie Chart) ---
        plt.figure(figsize=(8, 8))
        resultados['canales'].plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Distribución de Ventas por Canal')
        plt.ylabel('') # Quitar etiqueta lateral
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}reporte_canales.png")
        plt.close()

        # --- Gráfico 2: Ingresos por Sede (Bar Chart) ---
        plt.figure(figsize=(10, 6))
        resultados['por_sede'].plot(kind='bar', color='coral')
        plt.title('Ingresos Netos por Sede')
        plt.xlabel('Sede')
        plt.ylabel('Monto ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}reporte_sedes.png")
        plt.close()

        print(f"✅ Gráficos guardados en la carpeta: {self.output_dir}")