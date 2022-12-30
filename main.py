#!/usr/bin/env python3
from urllib.parse import urlsplit, parse_qs, parse_qsl

def parse_url(url: str) -> dict:
    return dict(parse_qsl(urlsplit(url).query))

if __name__ == '__main__':
    assert parse_url('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_url('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse_url('http://example.com/') == {}
    assert parse_url('http://example.com/?') == {}
    assert parse_url('http://example.com/?name=Dima') == {'name': 'Dima'}
  

def parse_cookie(query: str) -> dict:
    return dict(parse_qsl(urlsplit(query).path, separator=';'))

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}