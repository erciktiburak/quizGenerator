from flask import Flask, render_template, request

app = Flask(__name__)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("Who is the author of 'Romeo and Juliet'? ", "William Shakespeare"),
    Question("What is the largest mammal? ", "Blue whale")
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    for question in questions:
        user_answer = request.form.get(question.prompt.strip('? '))
        if user_answer.lower() == question.answer.lower():
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
