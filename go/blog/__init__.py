from flask import Flask
from flask_bootstrap import Bootstrap

 

app=Flask(__name__)
Bootstrap(app)




from blog import routes
from blog import forms

