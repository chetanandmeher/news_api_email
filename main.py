# import the requests lib to get the webpages using their url-- Requests allows you to send HTTP/1.1 requests
# extremely easily
# we can get the information from APIs using this lib in a readable way
import requests
from  send_email import send_email
# store the api key and url in usable variable
api_key = "c92a3c1867644d00a6a0db54e60213c0"
url1 = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-07&sortBy=publishedAt&apiKey=c92a3c1867644d00a6a0db54e60213c0"
url2 = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=c92a3c1867644d00a6a0db54e60213c0"
# request to the api to get the content
request = requests.get(url1)

'''
# get the content in text formate
## content = request.text          # will get the content in text format
# NOTE :- using .json response instead of .text to get a dictionary format content
'''
content = request.json()

'''
#************* we can check everything using the debug terminal at the break point *************#
content:- dict_keys(['status', 'totalResults', 'articles'])
'status': 'ok',
'totalResults': 13725, 
'articles': articles[0]: dict_keys(['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])
            [{'source': {'id': None, 'name': 'Protothema.gr'}, 
              'author': None, 
              'title': 'Tesla: Άλλαξε την παραγωγή των αυτοκινήτων', 
              'description': # description of the topic 
              'url': 'https://www.protothema.gr/car-and-speed/article/1367295/tesla-allaxe-tin-paragogi-ton-autokiniton/', 
              'urlToImage': 'https://i1.prth.gr/images/640x360share/files/2023-05-04/230428154238_Tesla-megacasting.jpg', 
              'publishedAt': '2023-05-06T11:30:00Z', 
              'content': # the content of the topic}
            ]
'''

# get the title and description of the contents
# collect all the required data from the content dictionary to text format
news_body = ""
for item in content['articles']:
    news_body = news_body + 'Title: ' + item['title'] + "\n" \
                + 'Descr: '+ item['description'] + '\n' \
                + 'Url  : ' + item['url'] + 2*"\n"

# call the function for send email
send_email(message=news_body)
