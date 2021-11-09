from flask import Flask, render_template, request
import sqlite3

sqlite_file = 'doordash.sqlite'

app = Flask(__name__)

WEB_APP_NAME = "MIS320"

@app.route('/')
@app.route('/home')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)


@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    driver_ssn = request.form['driver_ssn']
    make = request.form['make']
    license_plate = request.form['license_plate']
    model = request.form['model']
    return render_template("data_added.html", field="Vehicle")


@app.route('/add_vehicle', methods=['GET'])
def login_page():
    return render_template("add_vehicle.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
