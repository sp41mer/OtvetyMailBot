from models.bot_models import Article, Question
from nlp import make_word_vector
from numpy import linalg as LA
import pandas as pd
import numpy as np
import re

#TODO: Make it in Python 3 because of unicode problems with Pandas

def scan_articles():
    for article in Article.select():
        article.inf_title = make_word_vector(re.sub("<.*?>", " ", article.title))
        article.inf_text = make_word_vector(re.sub("<.*?>", " ", article.text))
        article.save()

def make_answers():
    for question in Question.select().where(Question.isAnswered==False):
        #get vector of question title
        vector_of_title = set(question.inf_title.split(' '))
        list_of_vectors = []
        for article in Article.select():
            list_of_matches = []
            article_title_vector = article.inf_title.split(' ')
            each_word_counter = pd.Series(article_title_vector).value_counts()
            for word in vector_of_title:
                try:
                    counter = each_word_counter[word]
                    list_of_matches.append(counter)
                except Exception:
                    list_of_matches.append(0)
            list_of_vectors.append(list_of_matches)
        print(list_of_vectors)
        for vector in list_of_vectors:
            numpy_array = np.asarray(vector)
            print(LA.norm(numpy_array))

        #get vector of question content
        #make sets from it
        #look for mathes in each article
        #article with most matches - our answer


make_answers()
#scan_articles()
