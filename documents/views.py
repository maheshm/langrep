from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from documents.models import Document
from documents.models import Tag
import datetime

# Create your views here.
def index(request):
  doc_accessor = Document()
  docs = doc_accessor.collection.find()
  return render(request, 'documents/index.html', {"docs": docs, "count":docs.count()==0})

def show(request,id):
  doc_accessor = Document()
  doc = doc_accessor.find_by_id(id)
  #print doc.title
  return render(request, 'documents/show.html', {'doc': doc})

@login_required(login_url='/login')
def new(request):
  tags = Tag().collection.find({})
  return render(request, 'documents/new.html', {"tags":tags})

@login_required(login_url='/login')
def create(request):
  print request.POST
  doc = Document()
  doc_dict = doc.to_dict(request.POST, request.user.id)
  doc_obj = doc.collection.insert_one(doc_dict)
  return redirect('/documents/show/%s' % (doc_obj.inserted_id.__str__()))

@login_required(login_url='/login')
def edit(request):
  return render(request, 'documents/edit.html')

@login_required(login_url='/login')
def update(request):
  return render(request, 'documents/index.html')

#Tags
@login_required(login_url="/login")
def indexTag(request):
  tags = Tags().collection.find({})
  return render(request, 'documents/indexTag.html', {"tags", tags})

@login_required(login_url="/login")
def newTag(request):
  return render(request, 'documents/newTag.html')

@login_required(login_url='/login')
def createTag(request):
  print request.POST
  tag = Tag()
  tag_dict = doc.to_dict(request.POST, request.user.id)
  if tag_dict.parent == ObjectId("0"):
    tag_obj = doc.collection.insert_one(tag_dict)
  else:
    doc.collection.update_one({"_id":tag_dict.parent}, {$addToSet: {"sub_tag": {"name":tag_dict.name}}}, upsert=False)
  return redirect('/documents/indexTag')

#Login
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
