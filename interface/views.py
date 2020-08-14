from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'interface/index.html')

def room(request, room_name):
    return render(request, 'interface/room.html', {
        'room_name': room_name
    })