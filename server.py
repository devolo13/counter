from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Harry Potter was mid'


@app.route('/', methods=["GET"])
def counter():
    # IF USER HAS VISITED BEFORE INCREMENT SESSION COOKIE
    if 'visits' in session:
        session['visits'] += 1
    # IF FIRST TIME VISITOR CREATE SESSION COOKIE
    else:
        session['visits'] = 1
        session['fake_visits'] = 0
    return render_template('index.html', visits=session['visits'], fake_visits=session['fake_visits'])

@app.route('/plus_two_button', methods=["GET", "PUSH"])
def plus_two():
    # INCREMENT SESSION COOKIE THEN REDIRECT TO '/' FOR ADDITIONAL INCREMENTING
    session['visits'] += 1
    session['fake_visits'] += 2
    return redirect('/')

@app.route('/destroy_session')
def reset_session():
    # RESET SESSION COOKIE AND REDIRECT TO '/'
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
