from flask import Flask, render_template, request
import sqlite3

# TODO abstract this so it is only ran once
# sqlite_file = 'doordash_db.sqlite'
# conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()

# with open('testScript.sql', 'r') as sqlite_file:
  #  sql_script = sqlite_file.read()

# Inserts all tables used in database
# c.executescript(sql_script)

# c.execute("SELECT * FROM DRIVER")
# print(c.fetchall())
# c.execute('INSERT INTO DRIVER VALUES (54896465, "Mason", 0.0, 0.0, 0, 0.0, 0, 20)')
# c.execute("SELECT * FROM DRIVER")
# print(c.fetchall(), "here")
# c.close()

app = Flask(__name__)

WEB_APP_NAME = "MIS320"


@app.route('/')
@app.route('/home')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)


# TODO verify the data is correct, render an error template if data is entered incorrectly
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    print('Post Vehicle')
    driver_ssn = request.form['driver_ssn']
    make = request.form['make']
    license_plate = request.form['license_plate']
    model = request.form['model']
    # c.execute('INSERT INTO VEHICLE VALUES (?,?,?,?,?)', ('00001', driver_ssn, make, license_plate, model))
    print(driver_ssn, make, license_plate, model)
    return render_template("data_added.html", field="Vehicle")


@app.route('/add_vehicle', methods=['GET'])
def add_vehicle_page():
    print('Got Vehicle')
    return render_template("add_vehicle.html")


@app.route('/add_driver', methods=['POST'])
def add_driver():
    print('Post Driver')
    driver_ssn = request.form['driver_ssn']
    name = request.form['name']
    age = request.form['age']
    print(driver_ssn, name, age)
    return render_template("data_added.html", field="Driver")


@app.route('/add_driver', methods=['GET'])
def add_driver_page():
    print('Got Driver')
    return render_template("add_driver.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
