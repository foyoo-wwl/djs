from django.shortcuts import render

# Create your views here.
from .models import UserMessage

def getform(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        message = request.POST.get('message','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')

        user_message = UserMessage()
        user_message.name = name
        user_message.address = address
        user_message.email = email
        user_message.message = message
        user_message.object_id = 'hello'
        user_message.save()

    return render(request,'message_form.html')
    all_message = UserMessage.objects.all()
    for message in all_message:
        message.delete()
    return render(request, 'message_form.html')
