#!/usr/bin/env python3
from urllib.parse import urlsplit, parse_qs

def parse(query: str) -> dict:
    return dict((k, v if len(v)>1 else v[0]) for k, v in parse_qs(urlsplit(query).query).items())

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    '''gen_some_tests for 10 in tests do profit'''


def parse_cookie(query: str) -> dict:
    n = query.split(';')
    r = {}
    for i in n:
        if '=' in i:
            k, v = i.split('=', 1)
            if k in r:
                if isinstance(r[k], list):
                    r[k].append(k)
                else:
                    r[k] = [r[k], v]
            else:
                r[k] = v
    return r

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
