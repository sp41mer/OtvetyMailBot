from utils import delimiters
from models.bot_models import Article
import re
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def make_word_vector(text):
    first_vector = re.split('|'.join(delimiters), text)
    second_vector = [word for word in first_vector if len(word) > 3]
    result_vector = [morph.parse(word)[0].normal_form for word in second_vector]
    result = ' '.join(result_vector)
    return result




