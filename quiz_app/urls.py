from django.urls import path
from .views import QuizListView, QuizDetailView, QuizQuestionsView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('quizzes/<int:quiz_id>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('quizzes/<int:quiz_id>/questions/', QuizQuestionsView.as_view(), name='quiz-questions'),
]