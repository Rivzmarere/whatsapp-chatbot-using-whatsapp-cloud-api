from django.urls import path
from . import views

urlpatterns = [
    path("sendmessage", views.MessageSend.as_view()),
    path("6511a5fb-b5bb-416a-b9e4-d60795b0904a", views.MessageSendtwo.as_view(),name='whatsapp-webhook'),
]


#url -- https://1c0f-41-60-125-197.eu.ngrok.io/whatsapp/6511a5fb-b5bb-416a-b9e4-d60795b0904a
# token -- 55e085c1-b394-4972-b574-433f6877bb5d