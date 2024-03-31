from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin',default=False)

class DataProject(models.Model):
    judul = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='program/')
    bahasa = models.CharField(max_length=50)
    framework = models.CharField(max_length=50)
    uraian = models.TextField()
    demo = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return self.judul
    
class Pesan(models.Model):
    nama = models.CharField(max_length=50)
    nomor = models.CharField(max_length=20)
    komentar = models.TextField()

    def __str(self):
        return self.nama