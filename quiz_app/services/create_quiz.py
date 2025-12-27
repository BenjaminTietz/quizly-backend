import json
from quiz_app.models import Quiz, Question, QuestionOption
from .download_audio import download_audio
from .transcribe_audio import transcribe_audio
from .generate_quiz_ai import generate_quiz_from_transcript


def create_quiz_from_url(owner, url):

    audio_path = download_audio(url)
    transcript = transcribe_audio(audio_path)

    quiz_json = generate_quiz_from_transcript(transcript)

    if not quiz_json:
        raise ValueError("AI was unable to generate a quiz. Answer was empty, invalid, or blocked.")

    quiz_json = quiz_json.strip()

    try:
        quiz_data = json.loads(quiz_json)
    except Exception as e:
        raise ValueError("Invalid JSON received from AI.") from e

    quiz = Quiz.objects.create(
        owner=owner,
        title="Generated Quiz",
        description="Quiz generated from YouTube audio",
        video_url=url,
    )

    for q in quiz_data:
        question = quiz.questions.create(question_title=q["question_title"])
        for opt in q["options"]:
            question.options.create(
                option_text=opt,
                is_correct=(opt == q["answer"])
            )

    return quiz