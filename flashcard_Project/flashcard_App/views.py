from .models import Flashcard
from .models import Collections
from .serializers import FlashcardSerializer
from .serializers import CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class FlashcardList(APIView):

    def get(self, request):
        flashcard = Flashcard.objects.all()
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardCollection(APIView):

    def get(self, request):
        collection = Collections.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)





