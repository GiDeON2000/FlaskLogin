from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

if __name__ == "__main__":
    app.run(debug=True)