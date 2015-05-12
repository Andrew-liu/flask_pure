# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask.ext.script import Manager, Server
from app import app
from app.models import Post

manager = Manager(app)
manager.add_command("runserver", 
        Server(host="127.0.0.1", port=5000, use_debugger=True))

@manager.command
def save_post():
    post = Post(author="Andrew liu", 
        title="Hello World",
        tags="test",
        content="This is the First Post")
    to.save()

if __name__ == '__main__':
    manager.run()
