from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')
def users_t(request):
	return render(request,'status.html')	