from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:malek74831854@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))
@app.route('/')
def index():
    #fruits=["apple","grapes","berries","oranges"]
    #return render_template('index.html',quote='Kindness needs no translaction',fruits=fruits)
    result = Favquotes.query.all()
    return render_template('index.html', result=result)
#@app.route('/about')
#def about():
    #return '<h1> Hello world from about page</h1>'
@app.route('/quotes')
def quotes():
    #return '<h1> Life is journey </h1>'
    return render_template('quotes.html')
@app.route('/process', methods = ["POST"])
def process():
    #return '<h1> Life is journey </h1>'
    #if request.method == "POST":
    author= request.form['author']
    quote= request.form['quote']
    quotedata= Favquotes(author=author , quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    #return render_template('quotes.html')
    return redirect(url_for('index'))
