from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
	
	return render(request, 'log/home.html')
def reg(request,id):
	all_users=User.objects.get(id=id)
	context={
		'all':all_users
	}
	return render(request, 'log/sucess.html', context)
def process(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		if request.method == 'POST':
			first_name=request.POST['fname']
			last_name=request.POST['lname']
			email=request.POST['email']
			hpassword=bcrypt.hashpw(request.POST['pword'].encode(),bcrypt.gensalt())
			user=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hpassword)
		return redirect('/reg/'+str(user.id))
def login(request):
	if request.method=='POST':
		pings = User.objects.login_validator(request.POST)
		if len(pings):
			for tag, error in pings.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')
		else:
			user=User.objects.get(email=request.POST['email'])
			print user
			return redirect('/reg/'+str(user.id))