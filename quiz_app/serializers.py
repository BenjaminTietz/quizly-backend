from rest_framework import serializers
from .models import Quiz, Question, QuestionOption


class QuestionSerializer(serializers.ModelSerializer):
    question_options = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "id",
            "question_title",
            "question_options",
            "answer",
            "created_at",
            "updated_at",
        ]

    def get_question_options(self, obj):
        return [opt.option_text for opt in obj.options.all()]

    def get_answer(self, obj):
        correct_option = obj.options.filter(is_correct=True).first()
        return correct_option.option_text if correct_option else None
    

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "description",
            "video_url",
            "created_at",
            "updated_at",
            "questions",
        ]