from django.urls import path
from . import views


urlpatterns = [
    path('flashcard_app/', views.FlashcardList.as_view()),
    path('flashcard_app/', views.FlashcardCollection.as_view()),
]
