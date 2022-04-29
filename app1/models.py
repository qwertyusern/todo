from django.db import models
class Student(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    kurs = models.CharField(max_length=30,blank=True)
    raqam= models.PositiveSmallIntegerField(default=0,unique=True)
    def __str__(self):
        return self.ism
class Reja(models.Model):
    st = models.ForeignKey(Student,on_delete=models.CASCADE,max_length=30)
    sana = models.DateField(max_length=30,blank=True)
    bajarilgan = models.BooleanField(default=False)
    malumot = models.TextField()
    raqam= models.PositiveSmallIntegerField(default=0,unique=True)
    def __str__(self):
        return self.ism

