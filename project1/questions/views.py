from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question
import random

def home(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        answer_text = request.POST.get('answer')
        if question_text and answer_text:
            Question.objects.create(question_text=question_text, answer_text=answer_text)
    questions = Question.objects.all()
    return render(request, 'questions/home.html', {'questions': questions})

def get_random_question(request):
    questions = list(Question.objects.all())
    if questions:
        random_question = random.choice(questions)
        return JsonResponse({
            'question': random_question.question_text,
            'answer': random_question.answer_text
        })
    return JsonResponse({'error': 'No questions available'}, status=404)

def check_answer(request):
    user_answer = request.POST.get('user_answer')
    correct_answer = request.POST.get('correct_answer')
    is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
    return JsonResponse({'is_correct': is_correct, 'correct_answer': correct_answer})