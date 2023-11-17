from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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
