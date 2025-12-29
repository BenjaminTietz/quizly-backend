from django.db import models
from django.conf import settings


class Quiz(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the title of the quiz as a string.
        
        :return: The title of the quiz
        :rtype: str
        """
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the title of the question as a string.
        
        :return: The title of the question
        :rtype: str
        """
        return self.question_title
    

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the question option.

        The string representation includes the option text and its correctness.

        :return: A string representation of the question option
        :rtype: str
        """
        return f"{self.option_text} ({'correct' if self.is_correct else 'wrong'})"