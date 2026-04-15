from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenue sur mon API", "status": "ok"})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"message": f"Bonjour {name} !"})


@app.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a, b):
    return jsonify({"result": a + b})
