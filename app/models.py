from app import db
import datetime

class Post(db.Document):
    author = db.StringField(max_length=50)
    title = db.StringField(max_length=120, required=True)
    tags = db.ListField(db.StringField(max_length=30))
    time = db.DateTimeField(default=datetime.datetime.now())
    content = db.StringField()
