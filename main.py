#!/usr/bin/env python3
from urllib.parse import urlsplit, parse_qsl

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
    return dict(parse_qsl(urlsplit(query).path, separator=';'))

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('i=00;p=***&^%') == {'id': '00', 'p': '***&^%'}
    assert parse_cookie('i=01;;;;p=!@\/\/\//\///') == {'id': '01', 'p': '!@\\/\\/\\//\\///'}
    assert parse_cookie(';;;;;;') == {}
    assert parse_cookie('user=asd;;lastn=ddd;ad=vvv') == {'user': 'asd', 'lastn': 'ddd', 'ad': 'vvv'}
    assert parse_cookie('d=1;d=2') == {'d': '2'}
    assert parse_cookie('1=1;2=2') == {'1': '1', '2': '2'}
    assert parse_cookie('io======;d') == {'io': '====='}
    assert parse_cookie('fghjkl=ddf;;;') == {'fghjkl': 'ddf'}
    assert parse_cookie('!@$%^&*()_+=0000') == {'!@$%^&*()_ ': '0000'}
    assert parse_cookie('--;--') == {}
    