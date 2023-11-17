from flask import Flask, render_template, request, jsonify
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


@app.route('/translate', methods=['POST'])
def translate():
    # Dummy translation function - Replace this with your translation logic
    data = request.get_json()
    text_to_translate = data.get('text', '')
    # Replace this with actual translation logic
    translated_text = f"Translated: {text_to_translate}"

    return jsonify({'translated_text': translated_text})


# if __name__ == '__main__':
#     app.run(debug=True)
