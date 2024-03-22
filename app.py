from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de mon projet"

@app.route('/get', methods=['GET'])
def get_endpoint():
    return "Ceci est un endpoint GET"

@app.route('/post', methods=['POST'])
def post_endpoint():
    data = request.get_json()
    return f"Vous avez posté: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
