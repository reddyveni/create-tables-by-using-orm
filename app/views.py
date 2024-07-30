from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q


def dp_emp_mgr(request):
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    LEDO=Emp.objects.select_related('deptno').filter(ename__contains='R')
    LEDO=Emp.objects.select_related('deptno').filter(ename__in=('SMITH','SCOTT'))
    LEDO=Emp.objects.select_related('deptno').filter(sal__gt=120)
    LEDO=Emp.objects.select_related('deptno').filter(sal__lt=5000)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(sal__lte=5000)
    LEDO=Emp.objects.select_related('deptno').filter(sal__gte=1200)
    LEDO=Emp.objects.select_related('deptno').filter(ename='SMITH',sal=1200,job='CLERK')
    LEDO=Emp.objects.select_related('deptno').filter(Q(ename='SMITH') | Q(job='CLERK') | Q(sal=120))
    LEDO=Emp.objects.select_related('deptno').filter(Q(ename='SMITH') &  Q(job='CLERK') | Q(sal=120))
    LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='research')
    LEDO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SMITH')
    LEDO=Emp.objects.select_related('deptno','mgr').filter(mgr=2)




