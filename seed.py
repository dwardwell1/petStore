"""Seed file to make sample data for db."""

from models import *
from app import app

# Create all tables
db.drop_all()
db.create_all()

p1 = Pet(name="Petey", species='Dog', photo_url='https://i1.sndcdn.com/avatars-000103501656-iji6a5-t500x500.jpg',
         age=10, notes='THis is one dumbass dog')

p2 = Pet(name="Shjrump", species='Cat', photo_url='https://m.media-amazon.com/images/I/51mzfBqVdoL.jpg',
         age=4, notes='This dog is a fyyuckin cartoon')
p3 = Pet(name="Dumbass", species='porcupine', photo_url='https://dogbreedreview.com/wp-content/uploads/2020/05/Chihuahua.jpg',
         age=9, notes='This dog got no damn brain', available=False)

db.session.add_all([p1, p2, p3])
db.session.commit()
