from flask import Flask, render_template, request

app = Flask(__name__)

WEB_APP_NAME = "MIS320"

@app.route('/')
@app.route('/home')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
