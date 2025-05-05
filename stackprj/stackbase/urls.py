from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView

app_name='stackbase'

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    
    path('questions/<int:pk>/',QuestionDetailView.as_view(), name='question-detail'), 
    
]

