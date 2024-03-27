from django.db import models

# Create your models here.
#  Company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField( max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobiles Phones','Mobile Phones')))              
    added_date=models.DateTimeField( auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name+"  --  "+self.location

class Employee(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    phone=models.IntegerField()
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('Manager','Manger'),('Software Devloper','Sl'),('Product Leader','pl')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    