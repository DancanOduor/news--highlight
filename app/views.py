from flask import render_template
from app import app

# Views
@app.route('/news/<int:news_id>')
def index(news_id):

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)