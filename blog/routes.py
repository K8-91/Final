from flask import request, redirect, url_for, render_template
from blog import app
from blog.models import Entry
from blog.base_functions import get_post, add_post

@app.route('/')
def homepage():
    posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", posts=posts)


@app.route('/edit-post/', methods=["GET", "POST"])
def new_post():
    get_post()
    if request.method == "POST":
        add_post()
        return redirect((url_for("homepage")))
    return render_template('entry_form.html', form=get_post())

@app.route('/edit-post/<int:id>', methods=["GET", "POST"])
def exist_post(id=id):
    get_post(id)
    if request.method == "POST":
        add_post(id)
        return redirect((url_for("homepage")))
    return render_template('update_form.html', form=get_post(), post=Entry.query.filter_by(id=id).first())



if __name__ == "__main__":
    app.run(debug=True)