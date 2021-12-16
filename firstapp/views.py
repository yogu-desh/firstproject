from django.shortcuts import render 
from django.http import HttpResponse 
# import datetime 
#  # Create your views here. 
# def time_info_view(request): 
#     time=datetime.datetime.now() 
#     s='<h1>Hello Current Date and Time is :'+str(time)+'</h1>' 
#     return HttpResponse(s)

# def greetings_view(request): 
#      #total html code 1000 lines of code 
#     return HttpResponse('<h1>Hello Friends Good Morning...Have a Nice Day</h1')
def wish(request): 
    return render(request,'firstapp/wish.html')