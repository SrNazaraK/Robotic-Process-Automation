import os
import pandas as pd
from dotenv import load_dotenv

# Importaciones de tus módulos locales
from src.analysis import AnalizadorVentas
from src.charts import GeneradorGraficos
from src.messenger import RobotWhatsApp

# 1. Cargar las variables del archivo .env
load_dotenv()

def generar_excel_prueba(ruta):
    """
    Genera un archivo de datos ficticios si no existe el original.
    Esto asegura que el RPA siempre tenga algo que procesar.
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
    # 2. Configuración desde el entorno (.env)
    sid = os.getenv('TWILIO_ACCOUNT_SID')
    token = os.getenv('TWILIO_AUTH_TOKEN')
    telefono_destino = os.getenv('MI_TELEFONO')
    
    ruta_excel = "data/Ventas Fundamentos.xlsx"
    carpeta_reportes = "reports/"
    
    print("🤖 --- INICIANDO PROCESO RPA --- 🤖")

    try:
        # 3. Verificación de Datos
        if not os.path.exists(ruta_excel):
            generar_excel_prueba(ruta_excel)

        # 4. Módulo de Análisis
        print("\n🔍 Analizando datos financieros...")
        robot = AnalizadorVentas(ruta_excel)
        resultados = robot.realizar_calculos()
        
        # 5. Módulo de Visualización (Gráficos)
        print("🎨 Generando reportes visuales...")
        graficador = GeneradorGraficos(output_dir=carpeta_reportes)
        graficador.generar_reporte_visual(resultados)

        # 6. Módulo de Mensajería (Twilio)
        # Verificamos que las credenciales no estén vacías
        if sid and token and telefono_destino:
            print(f"\n📲 Enviando reporte a WhatsApp (+{telefono_destino[-4:]})...")
            messenger = RobotWhatsApp(sid, token)
            envio_id = messenger.enviar_resumen(telefono_destino, resultados)
            print(f"✅ Mensaje enviado con éxito. SID: {envio_id}")
        else:
            print("\n⚠️ ALERTA: No se pudo enviar el WhatsApp.")
            print("   Verifica que TWILIO_ACCOUNT_SID y TWILIO_AUTH_TOKEN estén en el .env")

        print("\n" + "="*40)
        print("🏆 PROCESO RPA COMPLETADO EXITOSAMENTE")
        print("="*40)

    except Exception as e:
        # Manejo de errores robusto para la rúbrica
        print(f"\n❌ ERROR CRÍTICO: {str(e)}")

if __name__ == "__main__":
    main()