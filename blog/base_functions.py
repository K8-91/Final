from blog import db
from blog.models import Entry
from blog.forms import EntryForm
from flask import flash


def get_post(id=None):
    if id:
        post = Entry.query.filter_by(id=id).first()
        form = EntryForm(data={
            'title': post.title,
            'body': post.body,
            'is_published': post.is_published})
    else:
        form = EntryForm()
    return form

def add_post(id=None):
    if id:
        post = Entry.query.filter_by(id=id).first()
        form = EntryForm(data={
            'title': post.title,
            'body': post.body,
            'is_published': post.is_published})
        post.title = form.title.data
        post.body = form.body.data
        post.is_published = form.is_published.data
        if form.is_published.data:
            flash(f'Post "{form.title.data.upper()}" updated!')
        else:
            flash('Required box not checked. Post not added.')
    else:
        form = EntryForm()
        new_post = Entry(title=form.title.data, body=form.body.data, is_published=form.is_published.data)
        db.session.add(new_post)
        if form.is_published.data:
            flash(f'New post "{form.title.data.upper()}" added!')
        else:
            flash('Required box not checked. Post not added.')
    db.session.commit()
