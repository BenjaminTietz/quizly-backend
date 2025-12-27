from rest_framework import serializers
from .models import Question, Quiz


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'difficulty']

class FavoriteSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        fields = ['id', 'quiz']

class ProgressSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        fields = ['id', 'quiz', 'score', 'completed']