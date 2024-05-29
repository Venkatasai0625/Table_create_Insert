from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def Topic_Insert(request):
    TN=input("Enter topic_name_TN")
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    
    return HttpResponse("Topic_table data inserted success!")

"""
def Webpages_Insert(request):
    top_name=input("Enter topicname_top_name")
    to=Topic.objects.get_or_create(topic_name=top_name)[0]
    to.save()
     
    n=input("Enter name_n ")
    u=input("Enter url_u ")
    w=input("Enter wpages_w ")
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,wpages=w)[0]
    wo.save()
    
    return HttpResponse("Webpage_table data inserted success!")
"""

def Webpages_Insert(request):
    top_name=input("Enter topicname_top_name")
    
    #to=Topic.objects.get(topic_name=top_name)[0]
    #to.save()
    LTO=Topic.objects.filter(topic_name=top_name)
     
    n=input("Enter name_n ")
    u=input("Enter url_u ")
    w=input("Enter wpages_w ")
    if LTO:
        to=LTO[0]
        wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,wpages=w)[0]
        wo.save()
        QLWO=Webpage.objects.all()
        d={"QLWO": QLWO}
        return render(request,'display_webpages.html',d)

    else:
        return HttpResponse('Given top_name is not  present in parent table')


def AccessRecord_Insert(request):
    tname=input("Enter topicname_top_name")
    tobj=Topic.objects.get_or_create(topic_name=tname)[0]
    tobj.save()
     
    N=input("Enter name_N ")
    U=input("Enter url_U ")
    W=input("Enter wpages_W ")
    wobj=Webpage.objects.get_or_create(topic_name=tobj,name=N,url=U,wpages=W)[0]
    wobj.save()
    
    D=input("Enter date_D")
    A=input("Enter Author_A")
    Aobj=AccessRecord.objects.get_or_create(name=wobj,date=D,author=A)[0]
    Aobj.save()
    
    return HttpResponse("AccessRecord_table data inserted success!")

def display_topics(request):
    QLTO=Topic.objects.all()
    d={"QLTO":QLTO}
    return render(request,"display_topics.html",context=d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
   # QLWO=Webpage.objects.exclude(topic_name='cricket')
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('-topic_name')
    QLWO=Webpage.objects.all().order_by('topic_name')
    #QLWO=Webpage.objects.all().order_by('topic_name')[2:5]
    #QLWO=Webpage.objects.all()[3:7]
    
    #QLWO=Webpage.objects.filter(topic_name__startswith='R')
    QLWO=Webpage.objects.filter(name__endswith='i')
    QLWO=Webpage.objects.filter(url__contains=':')
    #QLWO=Webpage.objects.filter(name__in='sai')
    #QLWO=Webpage.objects.filter(topic_name__startswith='cric')
    
    #QLWO=Webpage.objects.filter(topic_name__endswith='et')
    #QLWO=Webpage.objects.filter(='cric')
    
    
    
    
    
    
    
    d={"QLWO": QLWO}
    return render(request,'display_webpages.html',d)

def display_Access_Record(request):
    QLAO=AccessRecord.objects.all()
    #QLAO=AccessRecord.objects.filter()
    #QLAO=AccessRecord.objects.filter(date__year=2000)
    
    #QLAO=AccessRecord.objects.filter(date__month=1)
    QLAO=AccessRecord.objects.filter(date__day=20-1)
    
    
    d={"QLAO": QLAO}
    return render(request,'display_Access_Record.html',d)