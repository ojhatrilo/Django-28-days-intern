from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question,Choice



def index(request):
    data = Question.objects.all()
    ans = Choice.objects.all()
    mylist = zip(data,ans)
    context = {
            'mylist': mylist,
        }
    
    return render(request, 'index.html', context)