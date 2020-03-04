from flask import Flask, session

from head_first_python.decorator.checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'Topestrafullah'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'User logged in'


@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'User logged out'


@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'User logged in'
    return 'User logged out'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3'


if __name__ == '__main__':
    app.run(debug=True)
