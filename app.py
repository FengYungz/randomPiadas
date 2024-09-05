from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from jokes import get_joke

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/joke', methods=['GET'])
def joke_route():
    language = request.headers.get('Accept-Language', 'pt-br').lower()
    if language not in ['en', 'pt-br']:
        language = 'pt-br'

    level = request.args.get('level', 'medium').lower()
    joke = get_joke(language, level)
    return jsonify({"joke": joke})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
