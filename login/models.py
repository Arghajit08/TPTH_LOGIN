from django.db import models
# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    team_name=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    organization=models.CharField(max_length=100,default="")
    phone_no=models.IntegerField(default=0)
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")


    count=models.IntegerField(default=0)

    def __str__(self):
        return self.team_name

class Photo(models.Model):
    id=models.AutoField(primary_key=True)
    file = models.FileField(upload_to='file')
    team_name=models.CharField(max_length=100)
    statement=models.CharField(max_length=100)
    def __str__(self):
        return self.statement