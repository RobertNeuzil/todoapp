from django.shortcuts import render

def index(request):
	return render(request, 'first/index.html')

# Create your views here.