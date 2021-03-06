from flask import Flask, render_template, request
from mysql import connector
from vvsearch import search4letters

app = Flask(__name__)

dbconfig = {'host': 'localhost',
            'user': 'vvsearchuser',
            'password': 'vvsearchpass',
            'database': 'vvsearchlog'}


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    conn = connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """select phrase, letters, ip, browser_string, results
                  from log"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
    cursor.close()
    conn.close()

    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    conn = connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
