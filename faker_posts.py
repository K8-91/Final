from faker import Faker
from blog.models import Entry
from blog import db


def fake_posts(quantity=10):
    fake = Faker()
    for i in range(quantity):
        new_post = Entry(title=fake.sentence(), body=fake.text(60), is_published=True)
        db.session.add(new_post)
        db.session.commit()

fake_posts()
