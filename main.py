from flask import Flask
import random
app = Flask(__name__)
facts_list = ["pootis",
        "huehuehuehue"]
@app.route("/")
def index():
    return f"<h1>opale</h1> <a href= '/random_fact' >¡potis&huehuehue!</a>"
@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)