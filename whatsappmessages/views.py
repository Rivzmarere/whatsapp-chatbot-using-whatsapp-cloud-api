import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .functions import sendWhatsappMessage

# Create your views here.

class MessageSend(GenericAPIView):
    def get(self, request:Request, format=None):
            phoneNumber = "263719412450"
            message = "its rivaldo marere from django"
            response = sendWhatsappMessage(phoneNumber,message)
            return Response(data=response, status=status.HTTP_200_OK)
class MessageSendtwo(GenericAPIView):
    def get(self, request:Request, format=None):
            VERIFY_TOKEN = 'xxxxxxxxxx'
            mode = request. GET ['hub.mode']
            token = request.GET ['hub.verify_token']
            challenge = request. GET ['hub. challenge']

            if mode == 'subscribe' and token == VERIFY_TOKEN:
                return HttpResponse (challenge, status=200) 
            else:
                return HttpResponse('error', status=403)
class MessageSendthree(GenericAPIView):
    def post(self, request:Request, format=None):
            data = json.loads (request. body)
            if 'object' in data and 'entry' in data:
                if data['object'] == 'Whatsapp_business_account':
                    try:
                        for entry in data['entry']:
                            phoneNumber = entry ['changes'][0]['value']['metadata']['display_phone_number']
                            phoneId = entry['changes'][0]['value']['metadata'] ['phone_number_id']
                            profileName = entry ['changes'] [0] ['value'] ['contacts'] [0] ['profile' ] ['name' ]
                            whatsAppId = entry['changes '] [0] ['value'] ['contacts'] [0] ['wa_id']
                            fromId = entry['changes'] [0] ['value '] ['messages '] [0] [' from']
                            messageId = entry['changes'] [0] ['value '] ['messages ' ] [0] ['" id']
                            timestamp = entry['changes'] [0] ['value'] ['messages'] [0] ['timestamp']
                            text = entry['changes'] [0] ['value'] ['messages'] [0] ['text '] ['body']


                            phoneNumber = "27828882737"
                            message = 'RE: [} was. received'. format (text)
                            sendWhatsappMessage (phoneNumber, message)
                    except:
                        pass

            return Response(data='Success', status=status.HTTP_200_OK)
    
    

