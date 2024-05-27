from django.shortcuts import render,redirect

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

def date(request):
    if request.method =="POST":
        question = request.POST['question_text']
        date = request.POST['pub_date']
        ans = request.POST['questions']
        choice = request.POST['choice_text']
        votes = request.POST['votes']

        data = Question(question_text=question, pub_date = date)
        data.save()
        ans = Choice(question=ans,choice_text=choice,votes=votes)
        ans.save()
        return redirect('hello')
    data = Question.objects.all()

    return render(request, 'time.html',{"question":data})


    # data = Question.objects.get(id=id)
    # return render(request, 'time.html',{"data":data})