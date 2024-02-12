from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def equi_join(request):
    EMPO=Emp.objects.select_related('dept_no').all()
    EMPO=Emp.objects.select_related('dept_no').filter(sal__gt=20000)
    EMPO=Emp.objects.select_related('dept_no').filter(dept_no__dept_name='Sales')
    EMPO=Emp.objects.select_related('dept_no').filter(mgr__isnull=True)
    EMPO=Emp.objects.select_related('dept_no').filter(comm__isnull=False)
    EMPO=Emp.objects.select_related('dept_no').filter(emp_name='Niharika')
    EMPO=Emp.objects.select_related('dept_no').filter(dept_no=10)
    EMPO=Emp.objects.select_related('dept_no').filter(sal__lt=40000)
    EMPO=Emp.objects.select_related('dept_no').filter(comm=0)
    EMPO=Emp.objects.select_related('dept_no').filter(emp_name__startswith='A')
    EMPO=Emp.objects.select_related('dept_no').filter(emp_name__endswith='n')
    EMPO=Emp.objects.select_related('dept_no').filter(emp_name__endswith='N')
    EMPO=Emp.objects.select_related('dept_no').order_by('emp_name')
    EMPO=Emp.objects.select_related('dept_no').order_by('-emp_name')
    EMPO=Emp.objects.select_related('dept_no').filter(emp_name__startswith='A',sal__gt=30000)
    EMPO=Emp.objects.select_related('dept_no').order_by(Length('emp_name'))
    EMPO=Emp.objects.select_related('dept_no').order_by(Length('emp_name').desc())
    EMPO=Emp.objects.select_related('dept_no').order_by(Length('emp_name'))[2::2] 
    d={'EMPO':EMPO}
    return render(request,'equi_join.html',d)

def self_join(request):
    EMO=Emp.objects.select_related('mgr').all()
    EMO=Emp.objects.select_related('mgr').filter(sal__gt=20000)
    EMO=Emp.objects.select_related('mgr').filter(sal__gte=30000)
    EMO=Emp.objects.select_related('mgr').filter(sal__lt=30000)
    EMO=Emp.objects.select_related('mgr').filter(sal__lte=30000)
    EMO=Emp.objects.select_related('mgr').order_by('emp_name')
    EMO=Emp.objects.select_related('mgr').order_by(Length('emp_name'))
    EMO=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EMO=Emp.objects.select_related('mgr').filter(mgr__emp_name__startswith='A')    
    EMO=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=True)
    EMO=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=False)
    EMO=Emp.objects.select_related('mgr').filter(mgr__comm=0)
    EMO=Emp.objects.select_related('mgr').filter(mgr__emp_name__startswith='A',sal__gt=30000).order_by(Length('emp_name'))
    EMO=Emp.objects.select_related('mgr').filter(Q(emp_name='Allen')| Q(emp_name='Black'))
    EMPO=Emp.objects.select_related('dept_no').order_by(Length('emp_name'))[2::2]
    d={'EMO':EMO}
    return render(request,'self_join.html',d)

def emp_mgr_dept(request):
    EMDO=Emp.objects.select_related('dept_no','mgr').all()
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(emp_name='Allen')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(emp_name='Allen',sal__gt=30000)
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(Q(emp_name='Black')|Q(sal__gt=40000))
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(dept_no__dept_name__startswith='R')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(mgr__emp_name__startswith='A')
    #EMDO=Emp.objects.select_related('dept_no','mgr').filter(mgr__dept_no=10,dept_name__endswith='k')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(emp_name__startswith='A',mgr__sal__gt=30000,dept_no=20)
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(dept_no__dept_location='New York')    
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(dept_no__dept_name='Research')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(emp_name='Black',dept_no__dept_location='New York')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(dept_no=10,dept_no__dept_location__endswith='k')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(mgr__dept_no=10)
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(mgr__dept_no=10,dept_no__dept_location__endswith='k')
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(mgr__dept_no=10,dept_no__dept_location__endswith='k',sal__gt=20000)
    EMDO=Emp.objects.select_related('dept_no','mgr').filter(dept_no__dept_name__endswith='N',mgr__dept_no=10,sal__gte=20000)
    d={'EMDO':EMDO}
    return render(request,'emp_mgr_dept.html',d)


def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=Salgrade.objects.all()
    #SO=Salgrade.objects.filter(grade=3)
    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))

    #EO=Emp.objects.none()
    #SO=Salgrade.objects.filter(grade=4)
    #for s in SO:
       # EO=EO|Emp.objects.filter(sal__range=(s.losal,s.hisal))
    
    #EO=Emp.objects.none()
    #SO=Salgrade.objects.filter(grade__in=(3,4))
    #for e in SO:
     #   EO=EO|Emp.objects.filter(sal__range=(e.losal,e.hisal))
    

    #EO=Emp.objects.none()
    #SO=Salgrade.objects.filter(grade__in=(3,4,5))
    #for so in SO:
     #   EO=EO|Emp.objects.filter(sal__range=(so.losal,so.hisal))



    EO=Emp.objects.none()
    SO=Salgrade.objects.filter(grade__in=(1,2,3))
    for so in SO:
        #EO=EO|Emp.objects.filter(Q(sal__range=(so.losal,so.hisal)) | Q(emp_name='Black'))
        EO=EO|Emp.objects.filter(sal__range=(so.losal,so.hisal))
        

    

    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)

