from flask import Flask, request, render_template, redirect
from music_type import MusicType

mt = MusicType(0, 0, 0, 0)

app = Flask(__name__)

@app.route("/nyla")
def hello_world(): 
    return "hello Nyla" 

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question(): 
    answers = ['slow','soft' ,'medium', 'fast']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)
    
    if request.method == 'POST':
        seleted = request.form['selected']
        if seleted == answers[0]:
            mt.add('country')
        if seleted == answers[1]:
            mt.add('rap')
        if seleted == answers[2]:
            mt.add('pop')
        if seleted == answers[3]:
            mt.add('r&b')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    answers = ['Dolly Parton','A boogie', 'Olivia Rodrigo', 'Brent Faiyaz']

    if request.method == 'GET': 
        return render_template('question_2.html', answers= answers)
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')