from django.shortcuts import render
from uuid import uuid4
from .models import Users,Role,Priority,Tickets

def generate_key():
	rand_token = uuid4()
	return rand_token

def validate_user(user:str):
	try:
		users=Users.objects.get(username=user)
		return True
	except:
		return False
	
def index(request):
	roles=Role.objects.all()
	context={
	'roles':roles
	}
	return render(request,'index.html',context)

def authorize(request):
	if request.method=='POST':
		user_name= request.POST["uname"]
		role_id=request.POST["role"]
		authtoken=str(generate_key())
		flag=validate_user(user_name)
		if flag:
			message="Sorry"+" "+user_name+" "+"is already present"+" "+"Please try with another username"
		else:
			
			user_object=Users(username=user_name,role_id=role_id,auth_token=authtoken)
			user_object.save()
			message="Hi"+" "+user_name+" "+"Your token was generated :"+authtoken
			
		context={
		'message':message
		}
		return render(request,'status.html',context) 
	else:
		roles=Role.objects.all()
		context={
		'roles':roles
		}
		return render(request,'index.html',context)       
		
