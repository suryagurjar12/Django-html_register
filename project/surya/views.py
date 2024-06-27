from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def register(request):
    return render(request,'register.html')
    
    
    
    
    
    
    
    
    
    
    # data={ "name":"surya","age":"24","Qualification":"post Graducation"
    #     }
    # return JsonResponse(data)
    