from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice

# List Questions and Choices
def index(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    mylist = zip(questions, choices)
    context = {
        'mylist': mylist,
    }
    return render(request, 'index.html', context)

# Create new Question and Choice
def create(request):
    if request.method == "POST":
        question_text = request.POST['question_text']
        pub_date = request.POST['pub_date']
        choice_text = request.POST['choice_text']
        votes = request.POST['votes']

        question = Question.objects.create(question_text=question_text, pub_date=pub_date)
        question.save()
        choice = Choice.objects.create(question=question, choice_text=choice_text, votes=votes)
        choice.save()
        return redirect('index')
    return render(request, 'create.html')

# Update existing Question and Choice
def update(request, question_id):
    question =Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    if request.method == "POST":
        question.question_text = request.POST['question_text']
        question.pub_date = request.POST['pub_date']
        question.save()

        choice_texts = request.POST.getlist('choice_text')
        votes = request.POST.getlist('votes')
        for choice, choice_text, vote in zip(choices, choice_texts, votes):
            choice.choice_text = choice_text
            choice.votes = vote
            choice.save()
        return redirect('index')

    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'update.html', context)

# Delete Question and related Choices
def delete(request, question_id):
    question = Question.objects.all(pk=question_id)
    if request.method == "POST":
        question.delete()
        return redirect('index')
    context = {
        'question': question,
    }
    return render(request, 'delete.html', context)
