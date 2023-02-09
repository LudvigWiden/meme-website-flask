from flask import Flask

app = Flask(__name__)

# Python decorator
@app.route("/")

def index():
    return "Drink more coffee RIGHT NOW!!"

# Run on our host, on port 80
app.run(host="0.0.0.0", port=80)








