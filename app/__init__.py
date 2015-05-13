# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flaskext.markdown import Markdown

app = Flask(__name__)  #创建Flask类的实例
app.config.from_object("config")  #从config.py读入配置
md = Markdown(app, 
            extensions=['footnotes'],
            entension_configs={'footnotes':('PLACE_MARKER', '```')},
            safe_mode=True,
            output_format='html4')
db = MongoEngine(app)  #实例化数据库

#这个import语句放在这里, 防止views, models import发生循环import
from app import views, models  

