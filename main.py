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
    assert parse_url('http://example.com/news/?id=1245&t=24:44:59&d=mm.dd.yy') == {'id': '1245', 't': '24:44:59', 'd': 'mm.dd.yy'}
    assert parse_url('http://example.com/news/?dasasd=35457&&&') == {'dasasd': '35457'}
    assert parse_url('http://example.com/news/???dasdas&dasdasdas&&') == {}
    assert parse_url('http://example.com/news/?hash=*****!@&gg=====') == {'hash': '*****!@', 'gg': '===='}
    assert parse_url('http://example.com/news/as/=11&uf-d') == {}
    assert parse_url('http://example.com/news/?man=id&help=me') == {'man': 'id', 'help': 'me'}
    assert parse_url('http://example.com/news/?id=12&z=33') == {'id': '12', 'z': '33'}
    assert parse_url('http://example.com/news/?id=22&22=z') == {'id': '22', '22': 'z'}
    assert parse_url('http://example.com/news/?id=5789&nnn=mmm') == {'id': '5789', 'nnn': 'mmm'}
    assert parse_url('http://example.com/news/?user=root&$%^&*()=42') == {'user': 'root', '*()': '42'}
    
    
  

def parse_cookie(query: str) -> dict:
    return dict(parse_qsl(urlsplit(query).path, separator=';'))

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}