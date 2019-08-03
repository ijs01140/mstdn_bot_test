#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mastodon import Mastodon
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(script_dir + '/settings.json', encoding="utf-8") as o:
    settings = json.load(o) #JSONを読む

mastodon = Mastodon(
client_id = script_dir + '/cred.txt', 
access_token = script_dir + '/auth.txt',
api_base_url = settings['url']) #インスタンス
mastodon.toot("なるほど") #ここを変える