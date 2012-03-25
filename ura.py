#!/usr/bin/env python
#coding: utf-8

from grab import Grab
from time import sleep

POSITION = 'Кот Юра'  # за что голосуем
POSITION_POS = 3  # порядковый номер позиции(нужен только для красивого вывода)
VOTES = 10  # количество накручивыемых голосов
G = Grab()


def id_for_answer(answer):
    """возвращает числовой идентификатор варианта ответа"""
    body = G.response.body
    ai = body.find(answer)
    fr = body[ai - 50: ai]
    id = fr[fr.find('PDI_answer') + 10:-2]
    return id


def vote(c, l, j, g, o, p, k, m, h, f):
    """голосуем..."""
    d = id_for_answer(POSITION)
    url = 'http://polldaddy.com/vote.php?va={}&pt={}&r={}&p={}&a={}&o=&t={}&token={}'.format(o, g, j, c, d, p, f)
    G.go(url)
    try:
        print G.css_text('.poll-msg'),
    except:
        print 'No msg',
    print G.css_list('.votes')[POSITION_POS - 1].text

#запускаем голосовалку
for i in range(0, VOTES):
    G.clear_cookies()
    G.go('http://polldaddy.com/poll/6061575/')
    vote_call = G.css_list('.button-lrg')[0].attrib['onclick']
    vote_call_args = vote_call[vote_call.find('(') + 1:vote_call.find(')')]
    vote_call_args = vote_call_args.strip().replace("'", '').split(',')
    vote(*vote_call_args)
    sleep(2)
