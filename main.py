import os
import pandas as pd
from src.analysis import AnalizadorVentas
from src.charts import GeneradorGraficos

def generar_excel_prueba(ruta):
    """
    Crea un archivo Excel ficticio para probar el RPA sin el archivo real.
    Cumple con las columnas necesarias para el análisis.
    """
    datos = {
        'Sede': ['Maracaibo', 'Caracas', 'Valencia', 'Maracaibo', 'Caracas', 'Maracaibo'],
        'Modelo': ['Toyota Corolla', 'Ford Fiesta', 'Toyota Corolla', 'Chevrolet Aveo', 'Ford Fiesta', 'Toyota Corolla'],
        'Cliente': ['Santiago', 'Juan', 'Maria', 'Santiago', 'Luis', 'Ana'],
        'Canal': ['Instagram', 'Web', 'WhatsApp', 'Instagram', 'Web', 'WhatsApp'],
        'Venta_sin_IGV': [20000, 15000, 20000, 12000, 15000, 20000],
        'Venta_con_IGV': [23200, 17400, 23200, 13920, 17400, 23200]
    }
    df = pd.DataFrame(datos)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df.to_excel(ruta, index=False)
    print(f"✅ Archivo de prueba generado en: {ruta}")

def main():
    # 1. Configuración de rutas
    ruta_excel = "data/Ventas Fundamentos.xlsx"
    carpeta_reportes = "reports/"
    
    print("🤖 --- INICIANDO PROCESO RPA --- 🤖")

    try:
        # 2. Verificar existencia del archivo o generar prueba
        if not os.path.exists(ruta_excel):
            generar_excel_prueba(ruta_excel)

        # 3. Módulo de Análisis
        print("\n🔍 Analizando datos financieros...")
        robot = AnalizadorVentas(ruta_excel)
        resultados = robot.realizar_calculos()
        
        # 4. Dashboard Resumen (Consola) - Punto 15 de la rúbrica
        print("\n" + "="*40)
        print("📊 DASHBOARD DE MÉTRICAS CLAVE")
        print("="*40)
        print(f"📈 Total de Ventas: {resultados['total_ventas']}")
        print(f"👥 Clientes Únicos: {resultados['clientes']}")
        print(f"💰 Ingresos Netos: ${resultados['total_sin_igv']:,.2f}")
        print(f"💸 Total con IGV:  ${resultados['total_con_igv']:,.2f}")
        print("-" * 40)
        print("📍 Ventas por Sede:")
        print(resultados['por_sede'])
        print("-" * 40)
        print("🚗 Top 5 Modelos:")
        print(resultados['top_5'])
        print("="*40)

        # 5. Módulo de Visualización (Puntos 11-14)
        print("\n🎨 Generando gráficos estadísticos...")
        graficador = GeneradorGraficos(output_dir=carpeta_reportes)
        graficador.generar_reporte_visual(resultados)

        # 6. Preparación para envío (Siguiente fase)
        print("\n✅ Proceso de análisis y visualización completado.")
        print(f"📁 Los reportes están listos en: {os.path.abspath(carpeta_reportes)}")

    except Exception as e:
        print(f"❌ Error crítico en la ejecución del RPA: {e}")

if __name__ == "__main__":
    main()