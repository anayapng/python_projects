# Creating a MCQ Quiz for practice. 

from AYQuestion import Question

# Creating my list of MCQ Questions and MCQ Options.
question_prompts = [
    'What is the best food for sore throat?\n(a) Honey\n(b) Chocolate\n(c) Durian\n\n',
    'Which food comes from Japan?\n(a) Odeng\n(b) Mochi\n(c) Smelly Tofu\n\n',
    'What is the most commonly drunk beverage in the mornings?\n(a) Soda\n(b) Tea\n(c) Coffee\n\n',
    'What are Muslims not allowed to eat?\n(a) Chicken\n(b) Pork\n(c) Beef\n\n',
    'What are Muslims encouraged to eat to break their fast with?\n(a) Crackers\n(b) Meat\n(c) Dates\n\n'
]

# Tracking the questions and the correct answers
questions_answers = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'c'),
    Question(question_prompts[3], 'b'),
    Question(question_prompts[4], 'c'),
]

def run_quiz(questions):
    score = 0
    for question in questions_answers:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('For this MCQ Quiz, you got '+ str(score) + '/' + str(len(questions_answers)) + ' correct')

print()
run_quiz(questions_answers)