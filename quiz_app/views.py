from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Quiz
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework.response import Response
from rest_framework import status
from quiz_app.services.create_quiz import create_quiz_from_url


class QuizCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({"detail": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

        quiz = create_quiz_from_url(owner=request.user, url=url)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        quizzes = Quiz.objects.filter(owner=request.user)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class QuizDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id, user):
        try:
            quiz = Quiz.objects.get(id=id)
        except Quiz.DoesNotExist:
            return None, Response(
                {"detail": "Quiz not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if quiz.owner != user:
            return None, Response(
                {"detail": "You do not have permission to access this quiz"},
                status=status.HTTP_403_FORBIDDEN
            )

        return quiz, None

    def get(self, request, id):
        quiz, error_response = self.get_object(id, request.user)
        if error_response:
            return error_response

        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        quiz, error_response = self.get_object(id, request.user)
        if error_response:
            return error_response

        serializer = QuizSerializer(quiz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        quiz, error_response = self.get_object(id, request.user)
        if error_response:
            return error_response

        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)