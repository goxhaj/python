#Install Flask
`python -m pip install flask`

#Create app in hello_flask.py with these contents:
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()

#Run flask
`python hello_flask.py`
