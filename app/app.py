from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "SRE Capstone v2 -Updated Via PR!"

@app.route("/health")
def health():
    if random.randint(1, 5) == 1:
        return "FAIL", 500
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# making a change
