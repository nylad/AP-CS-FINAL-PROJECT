from flask import Flask, request, render_template

import music_type

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
            music_type.add('country')
        if seleted == answers[1]:
            music_type.add('rap')
        if seleted == answers[2]:
            music_type.add('pop')
        if seleted == answers[3]:
            music_type.add('r&b')

            return
@app.route('/question/2', methods = ['GET', 'POST'])
def secound_question():
    answers = ['']
    
    if __name__ == '__main__':
    app.run(host='127.0.0.1')