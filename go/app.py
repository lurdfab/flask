from blog import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'thisisthekey'
db = SQLAlchemy(app)



class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False, unique=True)
    last_name = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True )
    comments = db.Column(db.String(length=1000), nullable=True, unique=True)
    password=db.Column(db.String(length=20), nullable=True, unique=True)

    
    def __repr__(self):
        return self.first_name


if __name__=="__main__":
    app.run(debug=True)