from django.db import models

# Create your models here.

class registermodel(models.Model):
    n_ame=models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=20)
    m_obile = models.IntegerField()
    a_ddress=models.CharField(max_length=50)
    #g_ender = models.CharField(max_length=10)
    p_wd=models.CharField(max_length=20)

class updatemodel(models.Model):
    p_hoto = models.ImageField(upload_to="app/static")
    n_ame = models.CharField(max_length=30)
    m_obile = models.IntegerField()
    a_ddress = models.CharField(max_length=50)
