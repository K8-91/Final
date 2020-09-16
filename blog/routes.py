from flask import Flask, request, redirect, url_for, render_template, flash
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm

@app.route('/')
def homepage():
    posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", posts=posts)


@app.route('/new-post', methods=["GET", "POST"])
def create_entry():
    form = EntryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = Entry(title=form.data['title'], body=form.data['body'], is_published=form.data['is_published'])
            db.session.add(new_post)
            db.session.commit()
            if form.data['is_published']:
                flash('New post added!')
            else:
                flash('Required box not checked. Post not added.')
        return redirect(url_for('homepage'))
    return render_template("entry_form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)