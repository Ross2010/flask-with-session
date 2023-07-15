from flask import Flask, request, render_template, redirect, flash, session, get_flashed_messages
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "pizdec"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.before_request
def setup_session():
    session['answers'] = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Start', methods=['POST'])
def start():
    return redirect('/question1')

@app.route('/Submit', methods=['POST'])
def submit():
    return redirect('/')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        radio_yes = request.form.get("radio_yes")
        radio_no = request.form.get("radio_no")
        if 'radio_yes' not in request.form and 'radio_no' not in request.form:
            flash("Make a selection!!!")
            return redirect('/question1')    
        elif radio_yes is not None:
            session['answers'].append(f"{satisfaction_survey.questions[0].question} - {radio_yes}")
        else:
            session['answers'].append(f"{satisfaction_survey.questions[0].question} - {radio_no}")
        return redirect('/question2')

    return render_template('question1.html', question=satisfaction_survey.questions[0].question, choices=satisfaction_survey.questions[0].choices)

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        radio_yes = request.form.get("radio_yes")
        radio_no = request.form.get("radio_no")
        if 'radio_yes' not in request.form and 'radio_no' not in request.form:
            flash("Make a selection!!!")
            return redirect('/question2')
        if radio_yes is not None:
            session['answers'].append(f"{satisfaction_survey.questions[1].question} - {radio_yes}")
        else:
            session['answers'].append(f"{satisfaction_survey.questions[1].question} - {radio_no}")
        return redirect('/question3')
    return render_template('question2.html', question=satisfaction_survey.questions[1].question, choices=satisfaction_survey.questions[1].choices)

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        radio_less = request.form.get("radio_less")
        radio_more = request.form.get("radio_more")
        if 'radio_less' not in request.form and 'radio_more' not in request.form:
            flash("Make a selection!!!")
            return redirect('/question3')
        if radio_less is not None:
            session['answers'].append(f"{satisfaction_survey.questions[2].question} - {radio_less}")
        else:
            session['answers'].append(f"{satisfaction_survey.questions[2].question} - {radio_more}")
        return redirect('/question4')

    return render_template('question3.html', question=satisfaction_survey.questions[2].question, choices=satisfaction_survey.questions[2].choices)

@app.route('/question4', methods=['GET', 'POST'])
def question4():
    if request.method == 'POST':
        radio_yes = request.form.get("radio_yes")
        radio_no = request.form.get("radio_no")
        if 'radio_yes' not in request.form and 'radio_no' not in request.form:
            flash("Make a selection!!!")
            return redirect('/question4')
        if radio_yes is not None:
            session['answers'].append(f"{satisfaction_survey.questions[3].question} - {radio_yes}")
        else:
            session['answers'].append(f"{satisfaction_survey.questions[3].question} - {radio_no}")
        return redirect('/answers')

    return render_template('question4.html', question=satisfaction_survey.questions[3].question, choices=satisfaction_survey.questions[3].choices)

@app.route('/answers', methods=['GET', 'POST'])
def show_answers():
    return render_template('answers.html')
