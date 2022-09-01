from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, "index.html")

def result(request):
    team_name=request.GET['team_name']
    name=request.GET['name']
    email=request.GET['email']
    password=request.GET['password']
    print(team_name,name,email,password)
    user = Register.objects.filter(email=email).first()
    user1=Register.objects.filter(team_name=team_name).first()
    if user is None:
        if user1:
            if user1.count<4:
                user1.count+=1
                data=request.GET
                print(data)
                serializer = UploadSerializers(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                user1.save()
                return HttpResponse('<h1>Team Registered</h1>')
            else:
                return HttpResponse('<h1>Team Limit Reached</h1>')
        else:
            serializer = UploadSerializers(data=request.GET)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponse('<h1>Team Registered</h1>')

    return HttpResponse('<h1>User Already Registered</h1>')

def login(request):
    return render(request, "second.html")

def login_result(request):
    email=request.GET['email']
    password=request.GET['password']
    print(email,password)
    user = Register.objects.filter(email=email).first()
    if user:
        if user.password==password:
            return redirect("https://tph2022.in/loggedin")
        else:
            return HttpResponse('<h1>Invalid Password!!</h1>')

    else:
        return HttpResponse('<h1>User Not Found!!</h1>')

def upload(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url = uploaded_file_url .replace("/media","")
        new_photo = Photo(
            file = uploaded_file_url,
            team_name=request.POST['team_name'],
            statement=request.POST['statement']

        )
        new_photo.save()
        return HttpResponse('<h1>File Uploaded.</h1>')
    else:
        return render(request, "third.html")



class GetView(APIView):
    def get(self, request):
        user = Register.objects.all()
        serializer = UploadSerializers(user,many=True)
        return Response(serializer.data)

class UploadView(APIView):
    def get(self, request):
        user = Photo.objects.all()
        serializer = PhotoSerializers(user,many=True)
        return Response(serializer.data)