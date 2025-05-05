from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class QuestionListView(ListView):
    model = Question
    template_name = 'stackbase/questions.html'
    context_object_name = 'questions'

class QuestionDetailView(DetailView):  
    model = Question
    template_name = 'stackbase/question_detail.html'
    context_object_name = 'question'
