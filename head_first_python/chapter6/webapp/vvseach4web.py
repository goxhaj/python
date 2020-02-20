from flask import Flask, render_template, request, escape
from vvsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '

    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search for vowel web page!!!')


@app.route('/viewlog')
def view_log() -> 'html':
    row_titles = ['REQUEST', 'REMOTE ADD', 'USER AGENT', 'RES']
    data = []
    with open('vvsearch.log') as log:
        for line in log:
            data.append(escape(line).split('|'))

    return render_template('viewlog.html', the_title='View Log page', the_row_titles=row_titles, the_data=data)


def log_request(req: 'flask_request', res: str) -> None:
    """
    'r' Open a file for reading. This is the default mode and, as such,
    is optional. When no second argument is provided, 'r' is assumed. It is also assumed that the file being read from already exists.

    'w' Open a file for writing. If the file already contains data, empty the file of its data before continuing.

    'a' Open a file for appending. Preserve the file’s contents, adding any new data to the end of the file (compare this behavior to 'w').

    'x' Open a new file for writing. Fail if the file already exists (compare this behavior to 'w' and to 'a')."""
    with open('vvsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


if __name__ == '__main__':
    app.run(debug=True)
