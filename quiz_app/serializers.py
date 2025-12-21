from rest_framework import serializers
from .models import Answer, Question, Category, Quiz, FavoriteQuiz, UserProgress

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'difficulty']

class FavoriteSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = FavoriteQuiz
        fields = ['id', 'quiz']

class ProgressSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = UserProgress
        fields = ['id', 'quiz', 'score', 'completed']