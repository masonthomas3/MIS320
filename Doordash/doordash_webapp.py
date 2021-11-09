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


# TODO verify the data is correct, make it render an error template if data is entered incorrectly
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


@app.route('/add_customer', methods=['POST'])
def add_customer():
    print('Post Customer')
    customer_name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']
    print(customer_name, phone_number, email, address)
    return render_template("data_added.html", field="Customer")


@app.route('/add_customer', methods=['GET'])
def add_customer_page():
    print('Got Customer')
    return render_template("add_customer.html")


@app.route('/add_payment_method', methods=['POST'])
def add_payment_method():
    print('Post Payment Method')
    customer_id = request.form['customer_id']
    card_number = request.form['card_number']
    expiration_date = request.form['expiration_date']
    security_number = request.form['security_number']
    print(customer_id, card_number, expiration_date, security_number)
    return render_template("data_added.html", field="Payment Method")


@app.route('/add_payment_method', methods=['GET'])
def add_payment_method_page():
    print('Got Payment Method')
    return render_template("add_payment_method.html")


@app.route('/add_payment', methods=['POST'])
def add_payment():
    print('Post Payment ')
    payment_method_id = request.form['payment_method_id']
    amount = request.form['amount']
    date = request.form['date']
    print(payment_method_id, amount, date)
    return render_template("data_added.html", field="Payment")


@app.route('/add_payment', methods=['GET'])
def add_payment_page():
    print('Got Payment')
    return render_template("add_payment.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
