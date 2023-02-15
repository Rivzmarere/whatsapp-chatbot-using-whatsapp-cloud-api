from django.conf import settings
import requests

def sendWhatsappMessage(phoneNumber , message):
    headers = {"Authorization":settings.WHATSAPP_TOKEN}
    payload ={ 
                "messaging_product": "whatsapp", 
                "to": phoneNumber, 
                "recipient_type": "individual", 
                 "type":"text",
                "text": { 
                            "body":message
                }
    }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    answer = response.json()
    return answer

    