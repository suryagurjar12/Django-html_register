from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse


def register(request):
    return render(request,'register.html')


def home(request):
    return redirect("https://www.google.com")
    
    
    
    
    
    
    
    
    
    
    # data={ "name":"surya","age":"24","Qualification":"post Graducation"
    #     }
    # return JsonResponse(data)
    