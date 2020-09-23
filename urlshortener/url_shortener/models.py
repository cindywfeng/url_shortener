import string
from random import choices

from .extensions import db


class URL(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    long_url = db.Column(db.String(800))
    short_url = db.Column(db.String(5), unique=True) # the part after base url

    #creating our 10 characters, randomly generated
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()
    
    # Generate the short-url link
    def generate_short_url(self):
        characters = string.digits + string.ascii_letters #whats ascii
        short_url = ''.join(choices(characters, k=5))
        
        # make sure it doesn't already exist
        link = self.query.filter_by(short_url = short_url).first()

        if link:
            return self.generate_short_url()

        return short_url