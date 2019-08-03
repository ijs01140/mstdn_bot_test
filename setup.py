#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mastodon import Mastodon
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(script_dir + '/settings.json', encoding="utf-8") as o:
    settings = json.load(o) #JSONを読む

url = settings['url'] #インスタンス先
Mastodon.create_app(settings['botname'], #クライアント名
api_base_url = url,
to_file = script_dir + '/cred.txt'
)
mastodon = Mastodon(
client_id= script_dir + '/cred.txt',
api_base_url = url
)
mastodon.log_in(
settings['user']['name'], #ログインメールアドレス
settings['user']['pass'], #パスワード
to_file = script_dir + '/auth.txt'
)