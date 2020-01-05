from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.template.loader import get_template
from .forms import *

def home_page(request):
	context = {"title": "select button"}
	return render(request, "home.html", context)

def logo_page(request):
	context = {"title": "Welcome to Ondream"}
	return render(request, "logo.html", context)



