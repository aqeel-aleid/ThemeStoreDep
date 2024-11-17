from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_view(request:HttpRequest):

    response =  render(request, "main/index.html")
    return response



def themes_view(request: HttpRequest):


    return render(request, "main/themes_page.html")


def contact_view(request: HttpRequest):

    return render(request, "main/contact_page.html")


def large_font_view(request: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("font", "large", max_age=60*60*24)

    return response


def normal_font_view(request: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("font", "large", max_age=-3600)

    return response

