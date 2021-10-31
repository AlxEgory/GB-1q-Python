# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choices
from random import sample


def get_jokes(n, repeat=True):
    """
    Generate jokes from 3 lists of 5 words
    :param n: number of jokes
    :param repeat: repeat the word in jokes
    :return: the list of 'n' jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat:
        nouns_mod = choices(nouns, k=n)
        adverbs_mod = choices(adverbs, k=n)
        adjectives_mod = choices(adjectives, k=n)
    else:
        if n > len(nouns):
            return 'The number of jokes cannot be more than the length of the list of unique words'
        nouns_mod = sample(nouns, k=n)
        adverbs_mod = sample(adverbs, k=n)
        adjectives_mod = sample(adjectives, k=n)
    jokes = []
    for noun, adverb, adjective in zip(nouns_mod, adverbs_mod, adjectives_mod):
        jokes.append(' '.join([noun, adverb, adjective]))
    return jokes


print(get_jokes(3, repeat=False))
