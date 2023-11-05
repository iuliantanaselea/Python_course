from flask import Flask, render_template
from api import tasks

app = Flask(__name__)
app.register_blueprint(tasks.bp)


@app.route("/about")
def about():
    return render_template("about.html", info="Info important")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
