from blog import app
from flask import render_template
from blog.forms import *



@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/contactus", methods=['GET', 'POST'])
def contact_us():
    form=ContactUsForm()
    if form.validate_on_submit():

        return '<h1>' + form.first_name.data + ' ' + form.last_name.data + ' ' + form.email.data + ' ' + form.comments.data + '</h1>'
    return render_template ("contact_us.html", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form=SignUpForm()
    if form.validate_on_submit():
        # new_user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=form.password.data)
        # db.session.add(new_user)
        # db.session.commit()
        
        return "<h2> New user has been created </h2>"
        # return '<h1>' + form.first_name.data + ' ' + form.last_name.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template ("signup.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():

        return '<h1>' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template ("/login.html", form=form)

@app.route("/blog")
def blog():
    return render_template ("/blog.html")