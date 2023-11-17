from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///translation.db'
# initialize the database
db = SQLAlchemy(app)

# making a translation class with text to translate and the translated texts


class Translate(db.Model):
    # set the primary key
    id = db.Column(db.Integer, primary_key=True)
    # text to be translated
    text_to_translate = db.Column(db.String(500), nullable=False)
    # the translated text
    text_translated = db.Column(db.String(500), nullable=False)
    # date of entry to the database
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # create function to return string when we add something
    def __repr__(self):
        return '<Name %r>' % self.id


# creatin of the database table within the application context.
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)


reversed_text = []


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    title = "Translation"
    # text = request.form['textToTranslate']
    text = request.form.get('textToTranslate')
    reversed_text.append("{}".format(text[::-1]))
    return render_template('index.html', reversed_text=reversed_text, title=title)
