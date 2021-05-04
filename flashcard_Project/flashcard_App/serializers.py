from rest_framework import serializers
from .models import Flashcard
from .models import Collections


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ["id", "word", "definition"]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ["id", "collection"]
