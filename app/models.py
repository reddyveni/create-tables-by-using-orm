from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    dloc=models.CharField(max_length=100)

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hiredate=models.DateField(auto_now=True)
    deptno=models.ForeignKey(Dept,on_delete=models.SET_NULL,null=True,blank=True)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
class salg(models.Model):
    grade=models.IntegerField(primary_key=True)
    hsal=models.DecimalField(max_digits=10,decimal_places=3)
    lsal=models.DecimalField(max_digits=10,decimal_places=2)

f