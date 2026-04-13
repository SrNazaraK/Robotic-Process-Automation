# 🤖 RPA: Análisis Financiero y Automatización de Notificaciones

Este proyecto implementa un sistema de **Robotic Process Automation (RPA)** desarrollado para la materia de **Inteligencia Artificial (2026A)** en la **Universidad Rafael Urdaneta (URU)**.

El sistema automatiza el flujo completo de gestión de datos: desde la extracción de información financiera en Excel, pasando por el análisis estadístico y visualización, hasta la notificación automática de resultados vía WhatsApp.

---

## 🚀 Funcionalidades Clave

1.  **Extracción de Datos:** Lectura automatizada de reportes de ventas en formato `.xlsx`.
2.  **Procesamiento de IA/Analítica:** Cálculo de métricas financieras (Ingresos netos, IGV, ventas por sede y modelos más vendidos).
3.  **Visualización:** Generación automática de gráficos estadísticos en la carpeta `reports/`.
4.  **Notificación RPA:** Envío de un dashboard resumen directamente a WhatsApp utilizando la API de **Twilio**.

---

### 📊 Sobre la Data
El sistema está optimizado para procesar el archivo `Ventas - Fundamentos.xlsx`, leyendo específicamente la hoja **VENTAS** para los cálculos financieros y generación de KPIs.

---

## 🛠️ Configuración y Despliegue (IMPORTANTE)

Para garantizar la seguridad y la portabilidad del proyecto, se ha implementado un sistema de **Variables de Entorno**. 

### 1. Configuración del archivo `.env`
No es necesario modificar el código fuente en `src/messenger.py`. El sistema está diseñado para leer toda la configuración desde un archivo centralizado.

1.  Localice el archivo `.env.example` en la raíz del proyecto.
2.  Renómbrelo a **`.env`**.
3.  Complete los siguientes campos con sus credenciales de Twilio:
    * `TWILIO_ACCOUNT_SID`: Su SID de cuenta de Twilio.
    * `TWILIO_AUTH_TOKEN`: Su Token secreto de autenticación.
    * `TWILIO_NUMBER`: El número de teléfono de su **Sandbox** de WhatsApp (ej. `+14155238886`).
    * `MI_TELEFONO`: El número de WhatsApp donde desea recibir el reporte (ej. `+58414XXXXXXX`).

### 2. Activación del Sandbox
Recuerde que antes de ejecutar el robot, debe vincular su teléfono al Sandbox de Twilio enviando el mensaje de activación correspondiente (ej. `join logic-exam`) al número de Twilio configurado.

---

## 📦 Instalación

```powershell
# 1. Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# 2. Instalar dependencias necesarias
pip install -r requirements.txt

# 3. Ejecutar el Robot
python main.py