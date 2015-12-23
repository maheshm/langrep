from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from documents.models import Document
import datetime

# Create your views here.
def index(request):
  docs = Document.objects.all()
  return render(request, 'documents/index.html', {"docs": docs, "count":len(docs)==0})

def show(request,id):
  doc = Document.objects.get(id=id)
  print doc.title
  return render(request, 'documents/show.html', {'doc': doc})

@login_required(login_url='/login')
def new(request):
  return render(request, 'documents/new.html')

@login_required(login_url='/login')
def create(request):
  print request.POST
  doc = Document(title=request.POST['title'],sub_title=request.POST["subtitle"],text=request.POST["content"],domain=request.POST["domain"],pub_date=datetime.datetime.now(), user=request.user )
  doc.save()
  return redirect('/documents/show/%i' % (doc.id))

@login_required(login_url='/login')
def edit(request):
  return render(request, 'documents/edit.html')

@login_required(login_url='/login')
def update(request):
  return render(request, 'documents/index.html')

def login(request):
  return render(request, 'login/login.html')

def login_do(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Logged in")
        else:
            return HttpResponse("Error: Account disabled")
    else:
      return HttpResponse("Invalid")

