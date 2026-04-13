from twilio.rest import Client

class RobotWhatsApp:
    def __init__(self, sid, token):
        """
        Inicializa el cliente de Twilio con las credenciales del .env
        """
        self.client = Client(sid, token)
        # ⚠️ IMPORTANTE: Asegúrate de que este número sea el que te dio el Sandbox de Twilio
        self.numero_twilio = 'whatsapp:+14155238886' 

    def enviar_resumen(self, destino, resultados):
        """
        Envía el reporte formateado a WhatsApp
        """
        # Extraemos los datos líderes para el mensaje
        sede_lider = resultados['por_sede'].idxmax()
        modelo_top = resultados['top_5'].idxmax()

        cuerpo = (
            f"🤖 *REPORTE AUTOMATIZADO RPA*\n\n"
            f"📈 *Ventas Totales:* {resultados['total_ventas']}\n"
            f"💰 *Ingresos Netos:* ${resultados['total_sin_igv']:,.2f}\n"
            f"📍 *Sede Líder:* {sede_lider}\n"
            f"🚗 *Modelo Top:* {modelo_top}\n\n"
            f"✅ Análisis generado desde Python (URU 2026)."
        )
        
        message = self.client.messages.create(
            body=cuerpo,
            from_=self.numero_twilio,
            to=f'whatsapp:{destino}'
        )
        return message.sid