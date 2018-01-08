#!/user/bin/env python
# -*- coding:utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse("XXXX!")
    context={}
    context['hello']='XXXXXXXXXXXX'
    return render(request,"welcome.html",context)