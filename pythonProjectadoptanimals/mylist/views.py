
# Create your views here.
from django.shortcuts import render
from .models import listsm
#import http in view
# Create your views here.
def my_list (request):
    contentlist = listsm.objects.all()
    print(contentlist)
    return render(request,"mylist.html",{"myylist":contentlist})