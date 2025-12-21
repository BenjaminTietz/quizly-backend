from django.urls import path
from .views import CategoryListView, QuizListView, QuizDetailView, QuizQuestionsView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('quizzes/<int:quiz_id>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('quizzes/<int:quiz_id>/questions/', QuizQuestionsView.as_view(), name='quiz-questions'),
]