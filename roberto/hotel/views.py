from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'hotel/index.html')

def room(request):
	return render(request, 'hotel/room.html')

def single(request):
	return render(request, 'hotel/single_room.html')

def about(request):
	return render(request, 'hotel/about.html')