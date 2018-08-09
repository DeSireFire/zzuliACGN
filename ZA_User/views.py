from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from django.core.paginator import Paginator,Page
from datetime import datetime

# Create your views here.

# 用户注册跳转
def Register(request):

    context = {'title': '用户注册'}
    # return  render(request,'ZA_users/RegEmail.html',context)