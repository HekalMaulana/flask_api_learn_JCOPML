from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Percobaan GET Request"

@app.route("/submit", methods=["POST"])
def submit():
    return "Percobaan POST Request"

if __name__ == "__main__":
    app.run(host="localhost", port="5000")
