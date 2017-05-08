from bs4 import BeautifulSoup
from models.bot_models import Article
import requests
import json
import re

class ArticleParser():
    def __init__(self):
        self.soup = ''

    def parse_url(self,url):
        self.url = url
        r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data)
        self.article = self.soup.findAll('article',{"class":'article__inner'})[0]
        self.title = self.parse_title()
        self.content = self.parse_content()
        self.hashtags = self.parse_hashtags()

    def parse_title(self):
        title_main = self.soup.findAll('h1')[0].text
        title_sub = self.article.findAll('p')[0].text
        title_string = title_main + '\n' + title_sub
        return title_string

    def parse_content(self):
        content_string = ''
        p_content = self.article.findAll('p')[1:]
        for p in p_content:
            content_string = content_string+p.text+'\n'
        ol_content = self.article.findAll('ol')
        for ol in ol_content:
            content_string = content_string+ol.text+'\n'
        ul_content = self.article.findAll('ul')
        for ul in ul_content:
            content_string = content_string + ul.text + '\n'
        return content_string

    def parse_hashtags(self):
        try:
            hashtags = self.article.findAll('ul',{"class":'htag'})[0].text
            hashtags_string = re.sub('\n','',hashtags)
        except:
            hashtags_string = '#'
        return hashtags_string

    def save_article(self):
        Article.create(
            href=self.url,
            title = self.title,
            text = self.content,
            keywords = self.hashtags
        )

url = "http://eshche.ru"
sitemap_url = "/sitemap.xml"
test_article_url = "/articles/online/prava-semi/nemnogo-ob-alimentnykh-obyazatelstvakh-i-sporakh"
r = requests.get(url+sitemap_url)
data = r.text
soup = BeautifulSoup(data)
list_locations = soup.findAll('loc')
for location in list_locations:
    if '/articles/' in location.text:
        try:
            article_parser = ArticleParser()
            article_parser.parse_url(url+location.text)
            article_parser.save_article()
            print(location.text)
        except:
            print('Fail '+location.text)

# r = requests.get(url+test_article_url)
# data = r.text
# soup = BeautifulSoup(data)
#
#
# zagolovok = soup.findAll('h1')[0].text
# print(zagolovok)
# podzagolovok = soup.findAll('article',{"class":'article__inner'})[0].findAll('p')[0].text
# print(podzagolovok)
# ostalnoi_abzac = soup.findAll('article',{"class":'article__inner'})[0].findAll('p')[1:]
# for element in ostalnoi_abzac:
#     print(element.text)
# vsyakie_spiski = soup.findAll('article',{"class":'article__inner'})[0].findAll('ol')
# for element in vsyakie_spiski:
#     print(element.text)
# hashtags = soup.findAll('article',{"class":'article__inner'})[0].findAll('ul',{"class":'htag'})[0].text
# hashtagsline = re.sub('\n','',hashtags)
# print(hashtagsline)

