from flask import render_template
from app import app
from.request import get_news

# Views
@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    

    political_news = get_news('political')
    general_news = get_news('general')
    agriculture_news = get_news('agriculture')
    bussines_news = get_news('business')
    celebrity_news = get_news('celebrity')
    title = 'Home - Welcome to The best News Website Online'


    # print(all_news)


    return render_template('index.html', title= title, political = political_news, general = general_news, agriculture = agriculture_news, business = bussines_news, celebrity = celebrity_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news page and its data
    '''
    news = get_news(id) 
    return render_template('news.html', news= news)

@app.route('/stories/<source_id>')
def stories(source_id):
    '''
    function that returns stories by source id
    '''

    story_source = get_stories(source_id)
    title = f'{source_id}| Stories'
    return render_template('stories.html',title = title, name = source_id, news = story_source )