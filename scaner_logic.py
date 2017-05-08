from models.bot_models import Article, Question
from list_of_answers import LIST_OF_ANSWERS
from nlp import make_word_vector, get_part_of_speech, get_word_for_answer
from numpy import linalg as LA
import pandas as pd
import numpy as np
import re
import random


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
            dict_of_matches = []
            article_title_vector = article.inf_title.split(' ')
            each_word_counter = pd.Series(article_title_vector).value_counts()
            for word in vector_of_title:
                try:
                    counter = each_word_counter[word]
                    list_of_matches.append(counter)
                    dict_of_matches.append({
                        'counter': counter,
                        'word': word
                    })
                except Exception:
                    list_of_matches.append(0)
            if len(dict_of_matches) > 0:
                top_word = sorted(dict_of_matches, key=lambda k: k['counter'], reverse=True)[0].get('word')
                if (get_part_of_speech(top_word)=='NOUN') & (LA.norm(np.asarray(list_of_matches)) > 1):
                    list_of_vectors.append({
                        'href': article.href,
                        'matches': list_of_matches,
                        'length': LA.norm(np.asarray(list_of_matches)),
                        'top_word': top_word
                    })
        sorted_list = sorted(list_of_vectors, key=lambda k: k['length'], reverse=True)
        list_for_answer=sorted_list[:3]
        if len(list_for_answer) > 0:
            try:
                answer_string = random.choice(LIST_OF_ANSWERS).format(get_word_for_answer(list_for_answer[0]['top_word']),list_for_answer[0]['href'])
                question.answer = answer_string
                question.save()
            except:
                print(question.href + ' ERROR!!!!')
                pass


make_answers()
# scan_articles()
