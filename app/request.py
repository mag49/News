from app import app
import urllib.request,json
from .models import news
News=news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        id = news_item.get('id')
        country = news_item.get('country')
        author = news_item.get('author')
        category= news_item.get('category')
        content = news_item.get('content')
        datePublished = news_item.get('datePublished')
        url = news_item.get('url')

        
        news_object = News(name, id, author,country, category,datePublished, content, url)
        news_results.append(news_object)

    return news_results

def get_stories(source_id):
    '''
    get story based on story source id
    '''

    get_story_url = stories_url.format(source_id, api_key)
    
    with urllib.request.urlopen(get_story_url) as url:
        get_stories_data = url.read()
        get_stories_response = json.loads(get_stories_data)

        stories_results = None

        if get_stories_response['stories']:
            stories_results_list = get_stories_response['story']
            stories_results = process_results(story_results_list)

    return stories_results


def process_source(story_list):
    '''
    '''
    stories_results = []
    for story_item in stories_list:
        title = story_item.get('title')
        description = story_item.get('content')
        image = story_item.get('image')
        datePublished = story_item.get('datePublished')
        author = story_item.get('author')
        url = story_item.get('url')


        if image:
            story_object = Articles(title, description, image, publishedAt, author, url)
            stories_stories.append(story_object)
            
    return stories_results

               