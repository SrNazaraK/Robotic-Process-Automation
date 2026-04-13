from twilio.rest import Client

class WhatsAppBot:
    def __init__(self, sid, token):
        self.client = Client(sid, token)

    def enviar_reporte(self, mensaje, media_url=None):
        from_whatsapp = 'whatsapp:++16624994095' 
        to_whatsapp = 'whatsapp:+584146182257'  
        
        message = self.client.messages.create(
            body=mensaje,
            from_=from_whatsapp,
            to=to_whatsapp,
            media_url=[media_url] if media_url else None
        )
        return message.sid