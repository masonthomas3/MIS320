from flask import Flask, render_template, request
import sqlite3

# TODO abstract this so it is only ran once
sqlite_file = 'doordash_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

with open('testScript.sql', 'r') as sqlite_file:
    sql_script = sqlite_file.read()

# Inserts all tables used in database
c.executescript(sql_script)

c.execute("SELECT * FROM DRIVER")
print(c.fetchall())
c.execute('INSERT INTO DRIVER VALUES (54896465, "Mason", 0.0, 0.0, 0, 0.0, 0, 20)')
c.execute("SELECT * FROM DRIVER")
print(c.fetchall(), "here")
c.close()

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
    c.execute('INSERT INTO VEHICLE VALUES (?,?,?,?)')
    return render_template("data_added.html", field="Vehicle")


@app.route('/add_vehicle', methods=['GET'])
def login_page():
    return render_template("add_vehicle.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
