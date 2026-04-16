from django.shortcuts import render

from .models import ChatRoom, ChatMessage


def index(request):
  chatrooms = ChatRoom.objects.all()
  return render(request, 'myapp/modern-index.html', {'chatrooms': chatrooms})


def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:25]
    return render(request,'myapp/modern-room.html',{'chatroom':chatroom, 'messages': messages})