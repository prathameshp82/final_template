from django.core.management.base import BaseCommand
from onlinecourse.models import Course, Question, Choice

class Command(BaseCommand):
    help = 'Creates a course with questions and choices'

    def handle(self, *args, **options):
        # Add the code for creating the course, questions, and choices here
        # Create a new course
        course = Course.objects.create(title="Python Programming")

        # Create questions for the course
        question1 = Question.objects.create(course=course, question_text="What is Python?")
        question2 = Question.objects.create(course=course, question_text="What is a variable?")

        # Create choices for each question
        choice1_q1 = Choice.objects.create(question=question1, choice_text="A programming language", is_correct=True)
        choice2_q1 = Choice.objects.create(question=question1, choice_text="A snake", is_correct=False)

        choice1_q2 = Choice.objects.create(question=question2, choice_text="A storage container for data", is_correct=True)
        choice2_q2 = Choice.objects.create(question=question2, choice_text="A type of snake", is_correct=False)


