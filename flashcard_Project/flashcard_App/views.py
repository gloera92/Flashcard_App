from django.shortcuts import render
from django.http import HttpResponse
from .models import Flashcard
# Create your views here.


def index(request):
    all_flashcards = Flashcard.objects.all()
    context = {
        'all_flashcards': all_flashcards
    }
    return render(request, 'flashcard_app/index.html', context)
