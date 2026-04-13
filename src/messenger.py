from twilio.rest import Client

class WhatsAppBot:
    def __init__(self, sid, token):
        self.client = Client(sid, token)

    def enviar_reporte(self, mensaje, media_url=None):
        from_whatsapp = 'whatsapp:+14155238886' # Número de prueba de Twilio
        to_whatsapp = 'whatsapp:+58412XXXXXXX'  # Tu número
        
        message = self.client.messages.create(
            body=mensaje,
            from_=from_whatsapp,
            to=to_whatsapp,
            media_url=[media_url] if media_url else None
        )
        return message.sid