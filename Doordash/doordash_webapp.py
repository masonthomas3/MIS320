from flask import Flask, render_template, request
import sqlite3


def set_up_database():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    with open('testScript.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    # Inserts all tables used in database
    c.executescript(sql_script)
    c.execute("SELECT * FROM DRIVER")
    for row in c:
        print(row)
    c.execute("SELECT * FROM CUSTOMER")
    for row in c:
        print(row)
    c.execute("SELECT * FROM doordash_order")
    for row in c:
        print(row)
    c.execute("SELECT * FROM vehicle")
    for row in c:
        print(row)
    c.execute("SELECT * FROM business")
    for row in c:
        print(row)
    c.execute("SELECT * FROM driver_payment")
    for row in c:
        print(row)
    c.execute("SELECT * FROM menu")
    for row in c:
        print(row)
    c.execute("SELECT * FROM menu_item")
    for row in c:
        print(row)
    c.execute("SELECT * FROM ordered_item")
    for row in c:
        print(row)
    c.execute("SELECT * FROM payment")
    for row in c:
        print(row)
    c.execute("SELECT * FROM payment_method")
    for row in c:
        print(row)
    c.close()


app = Flask(__name__)


WEB_APP_NAME = "MIS320"


@app.route('/')
@app.route('/home')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)


# TODO verify the data is correct, make it render an error template if data is entered incorrectly
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    driver_ssn = request.form['driver_ssn']
    make = request.form['make']
    license_plate = request.form['license_plate']
    model = request.form['model']

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    if len(driver_ssn) == 9 and make.isalpha() and 4 <= len(license_plate) <= 7:
        c.execute('INSERT INTO VEHICLE (Driver_SSN, Make, License_Plate, Model) '
                  'VALUES (?,?,?,?)', (driver_ssn, make, license_plate, model))
        c.execute('COMMIT')
        c.execute('SELECT * FROM vehicle')
        for row in c:
            print(row)
        return render_template("data_added.html", field="Vehicle")
    return render_template("data_invalid.html", field="Vehicle")


@app.route('/add_vehicle', methods=['GET'])
def add_vehicle_page():
    return render_template("add_vehicle.html")


@app.route('/add_driver', methods=['POST'])
def add_driver():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    driver_ssn = request.form['driver_ssn']
    name = request.form['name']
    age = request.form['age']
    if len(driver_ssn) == 9 and name.isalpha() and 2 <= len(age) <= 3:
        c.execute('INSERT INTO driver (Driver_SSN, Name, Age) '
                  'VALUES (?,?,?,?)', (driver_ssn, name, age))
        c.execute('COMMIT')
        c.execute('SELECT * FROM driver')
        for row in c:
            print(row)
        return render_template("data_added.html", field="Driver")
    return render_template("data_invalid.html", field="Driver")


@app.route('/add_driver', methods=['GET'])
def add_driver_page():
    return render_template("add_driver.html")


@app.route('/add_customer', methods=['POST'])
def add_customer():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    customer_name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']

    print(customer_name, phone_number, email, address)
    return render_template("data_added.html", field="Customer")


@app.route('/add_customer', methods=['GET'])
def add_customer_page():
    return render_template("add_customer.html")


@app.route('/add_payment_method', methods=['POST'])
def add_payment_method():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    customer_id = request.form['customer_id']
    card_number = request.form['card_number']
    expiration_date = request.form['expiration_date']
    security_number = request.form['security_number']

    print(customer_id, card_number, expiration_date, security_number)
    return render_template("data_added.html", field="Payment Method")


@app.route('/add_payment_method', methods=['GET'])
def add_payment_method_page():
    return render_template("add_payment_method.html")


@app.route('/add_payment', methods=['POST'])
def add_payment():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    payment_method_id = request.form['payment_method_id']
    amount = request.form['amount']
    date = request.form['date']

    print(payment_method_id, amount, date)
    return render_template("data_added.html", field="Payment")


@app.route('/add_payment', methods=['GET'])
def add_payment_page():
    return render_template("add_payment.html")


@app.route('/add_order', methods=['POST'])
def add_order():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    driver_ssn = request.form['driver_ssn']
    customer_id = request.form['customer_id']
    payment_id = request.form['payment_id']

    print(driver_ssn, customer_id, payment_id)
    return render_template("data_added.html", field="Order")


@app.route('/add_order', methods=['GET'])
def add_order_page():
    return render_template("add_order.html")


@app.route('/add_driver_payment', methods=['POST'])
def add_driver_payment():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    driver_ssn = request.form['driver_ssn']
    order_id = request.form['order_id']
    base_pay = request.form['base_pay']
    tip = request.form['tip']

    print(driver_ssn, order_id, base_pay, tip)
    return render_template("data_added.html", field="Driver Payment")


@app.route('/add_driver_payment', methods=['GET'])
def add_driver_payment_page():
    return render_template("add_driver_payment.html")


@app.route('/add_business', methods=['POST'])
def add_business():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    name = request.form['name']
    location = request.form['location']
    delivery_fee = request.form['delivery_fee']

    print (name, location, delivery_fee)
    return render_template("data_added.html", field="Business")


@app.route('/add_business', methods=['GET'])
def add_business_page():
    return render_template("add_business.html")


@app.route('/add_menu', methods=['POST'])
def add_menu():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    business_id = request.form['business_id']
    description = request.form['description']
    name = request.form['name']

    print(business_id, description, name)
    return render_template("data_added.html", field="Menu")


@app.route('/add_menu', methods=['GET'])
def add_menu_page():
    return render_template("add_menu.html")


@app.route('/add_menu_item', methods=['POST'])
def add_menu_item():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    menu_id = request.form['menu_id']
    name = request.form['name']
    cost = request.form['cost']

    print(menu_id, name, cost)
    return render_template("data_added.html", field="Menu Item")


@app.route('/add_menu_item', methods=['GET'])
def add_menu_item_page():
    return render_template("add_menu_item.html")


@app.route('/add_ordered_item', methods=['POST'])
def add_ordered_item():
    return render_template("data_added.html", field="Ordered Item")


@app.route('/add_ordered_item', methods=['GET'])
def add_ordered_item_page():
    return render_template("add_ordered_item.html")


if __name__ == "__main__":
    set_up_database()
    app.run(debug=True, host='0.0.0.0', port=8080)
