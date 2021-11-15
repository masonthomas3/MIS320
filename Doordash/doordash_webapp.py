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
    # c.execute("SELECT * FROM DRIVER")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM CUSTOMER")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM doordash_order")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM vehicle")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM business")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM driver_payment")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM menu")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM menu_item")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM ordered_item")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM payment")
    # for row in c:
    #     print(row)
    # c.execute("SELECT * FROM payment_method")
    # for row in c:
    #     print(row)
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
    driver_ssn = request.form['driver_ssn']
    make = request.form['make']
    license_plate = request.form['license_plate']
    model = request.form['model']

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT Driver_SSN FROM driver where Driver_SSN = {pk}'.format(pk=driver_ssn))
    row = c.fetchone()
    if row is not None:
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


@app.route('/display_vehicles', methods=['GET'])
def display_vehicles_page():
    header_row = "Vehicle_ID, Driver_SSN, Make, License Plate, Model"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM vehicle')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Vehicles", header_row=header_row, all_rows=all_rows)


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
                  'VALUES (?,?,?)', (driver_ssn, name, age))
        c.execute('COMMIT')
        c.execute('SELECT * FROM driver')
        for row in c:
            print(row)
        return render_template("data_added.html", field="Driver")
    return render_template("data_invalid.html", field="Driver")


@app.route('/add_driver', methods=['GET'])
def add_driver_page():
    return render_template("add_driver.html")


@app.route('/display_drivers', methods=['GET'])
def display_drivers_page():
    header_row = "Driver_SSN, Name, Age"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM driver')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Drivers", header_row=header_row, all_rows=all_rows)


@app.route('/add_customer', methods=['POST'])
def add_customer():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    customer_name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']

    if customer_name.isalpha() and phone_number.isnumeric():
        c.execute('INSERT INTO customer (Customer_Name, Phone_Number, Email, Address) '
                  'VALUES (?,?,?,?)', (customer_name, phone_number, email, address))
        c.execute('COMMIT')
        c.execute('SELECT * FROM customer')
        for row in c:
            print(row)
        return render_template("data_added.html", field="Customer")
    return render_template("data_invalid.html", field="Customer")


@app.route('/add_customer', methods=['GET'])
def add_customer_page():
    return render_template("add_customer.html")


@app.route('/display_customers', methods=['GET'])
def display_customers_page():
    header_row = "Customer ID, Name, Phone Number, Email, Address"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM customer')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Customers", header_row=header_row, all_rows=all_rows)


@app.route('/add_payment_method', methods=['POST'])
def add_payment_method():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    customer_id = request.form['customer_id']
    card_number = request.form['card_number']
    expiration_date = request.form['expiration_date']
    security_number = request.form['security_number']

    c.execute('SELECT Customer_ID FROM customer where Customer_ID = {pk}'.format(pk=customer_id))
    row = c.fetchone()
    if row is not None:
        if customer_id.isnumeric() and card_number.isnumeric() and (len(expiration_date) == 4 or len(expiration_date) == 5)\
                and security_number.isnumeric() and len(security_number) == 3:
            c.execute('INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number) '
                      'VALUES (?,?,?,?)', (customer_id, card_number, expiration_date, security_number))
            c.execute('COMMIT')
            c.execute('SELECT * FROM payment_method')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Payment Method")
    return render_template("data_invalid.html", field="Payment Method")


@app.route('/add_payment_method', methods=['GET'])
def add_payment_method_page():
    return render_template("add_payment_method.html")


@app.route('/display_payment_methods', methods=['GET'])
def display_payment_methods_page():
    header_row = "Payment_Method_ID, Customer ID, Card_Number, Expiration Date, Security_Number"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM payment_method')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Payment Methods", header_row=header_row, all_rows=all_rows)


@app.route('/add_payment', methods=['POST'])
def add_payment():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    payment_method_id = request.form['payment_method_id']
    amount = request.form['amount']
    date = request.form['date']

    c.execute('SELECT payment_method_id FROM payment_method where payment_method_id = {pk}'.format(pk=payment_method_id))
    row = c.fetchone()
    if row is not None:
        if payment_method_id.isnumeric() and amount.isnumeric() and len(date) == 10:
            c.execute('INSERT INTO payment (Payment_Method_ID, Amount, Date) '
                      'VALUES (?,?,?)', (payment_method_id, amount, date))
            c.execute('COMMIT')
            c.execute('SELECT * FROM payment')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Payment")
    return render_template("data_invalid.html", field="Payment")


@app.route('/add_payment', methods=['GET'])
def add_payment_page():
    return render_template("add_payment.html")


@app.route('/display_payments', methods=['GET'])
def display_payments_page():
    header_row = "Payment_ID, Payment_Method_ID, Amount, Date"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM payment')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Payments", header_row=header_row, all_rows=all_rows)


@app.route('/add_order', methods=['POST'])
def add_order():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    driver_ssn = request.form['driver_ssn']
    customer_id = request.form['customer_id']
    payment_id = request.form['payment_id']

    c.execute('SELECT Driver_SSN FROM driver where Driver_SSN = {pk}'.format(pk=driver_ssn))
    driver_row = c.fetchone()
    c.execute('SELECT Customer_ID FROM customer where Customer_ID = {pk}'.format(pk=customer_id))
    customer_row = c.fetchone()
    c.execute('SELECT Payment_ID FROM payment where Payment_ID = {pk}'.format(pk=payment_id))
    payment_row = c.fetchone()

    if driver_row is not None and customer_row is not None and payment_row is not None:
        if driver_ssn.isnumeric() and len(driver_ssn) == 9 and customer_id.isnumeric() and payment_id.isnumeric():
            c.execute('INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID) '
                      'VALUES (?,?,?)', (driver_ssn, customer_id, payment_id))
            c.execute('COMMIT')
            c.execute('SELECT * FROM doordash_order')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Order")
    return render_template("data_invalid.html", field="Order")


@app.route('/add_order', methods=['GET'])
def add_order_page():
    return render_template("add_doordash_order.html")


@app.route('/display_orders', methods=['GET'])
def display_orders_page():
    header_row = "Order ID, Driver SSN, Customer ID, Payment ID"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM doordash_order')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Orders", header_row=header_row, all_rows=all_rows)


@app.route('/add_driver_payment', methods=['POST'])
def add_driver_payment():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    driver_ssn = request.form['driver_ssn']
    order_id = request.form['order_id']
    base_pay = request.form['base_pay']
    tip = request.form['tip']

    c.execute('SELECT Driver_SSN FROM driver WHERE Driver_SSN = {pk}'.format(pk=driver_ssn))
    driver_row = c.fetchone()

    c.execute('SELECT Order_ID FROM order WHERE Order_ID = {pk}'.format(pk=order_id))
    order_row = c.fetchone()

    if driver_row is not None and order_row is not None:
        if driver_ssn.isnumeric() and len(driver_ssn) == 9 and order_id.isnumeric() \
                and base_pay.isnumeric() and tip.isnumeric():
            c.execute('INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip) '
                      'VALUES (?,?,?, ?)', (driver_ssn, order_id, base_pay, tip))
            c.execute('COMMIT')
            c.execute('SELECT * FROM driver_payment')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Driver Payment")
    return render_template("data_invalid.html", field="Driver Payment")


@app.route('/add_driver_payment', methods=['GET'])
def add_driver_payment_page():
    return render_template("add_driver_payment.html")


@app.route('/display_driver_payments', methods=['GET'])
def display_driver_payments_page():
    header_row = "Driver Payment ID, Driver SSN, Order ID, Base Pay, Tip"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM driver_payment')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Driver Payments", header_row=header_row, all_rows=all_rows)


@app.route('/add_business', methods=['POST'])
def add_business():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    name = request.form['name']
    location = request.form['location']
    delivery_fee = request.form['delivery_fee']

    if name.isalpha() and delivery_fee.isnumeric():
        c.execute('INSERT INTO business (Name, Location, Delivery_Fee) '
                  'VALUES (?,?,?)', (name, location, delivery_fee))
        c.execute('COMMIT')
        c.execute('SELECT * FROM business')
        for row in c:
            print(row)
        return render_template("data_added.html", field="Business")
    return render_template("data_invalid.html", field="Business")


@app.route('/add_business', methods=['GET'])
def add_business_page():
    return render_template("add_business.html")


@app.route('/display_businesses', methods=['GET'])
def display_businesses_page():
    header_row = "Business ID, Name, Location, Delivery_Fee"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM business')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Businesses", header_row=header_row, all_rows=all_rows)


@app.route('/add_menu', methods=['POST'])
def add_menu():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    business_id = request.form['business_id']
    description = request.form['description']
    name = request.form['name']

    c.execute('SELECT Business_ID FROM business WHERE Business_ID = {pk}'.format(pk=business_id))
    row = c.fetchone()
    if row is not None:
        if business_id.isnumeric():
            c.execute('INSERT INTO menu (Business_ID, Description, Name) '
                      'VALUES (?,?,?)', (business_id, description, name))
            c.execute('COMMIT')
            c.execute('SELECT * FROM menu')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Menu")
    return render_template("data_invalid.html", field="Menu")


@app.route('/add_menu', methods=['GET'])
def add_menu_page():
    return render_template("add_menu.html")


@app.route('/display_menus', methods=['GET'])
def display_menus_page():
    header_row = "Menu ID, Business ID, Description, Name"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM menu')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Menus", header_row=header_row, all_rows=all_rows)


@app.route('/add_menu_item', methods=['POST'])
def add_menu_item():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    menu_id = request.form['menu_id']
    name = request.form['name']
    cost = request.form['cost']

    c.execute('SELECT Menu_ID FROM menu WHERE Menu_ID = {pk}'.format(pk=menu_id))
    row = c.fetchone()
    if row is not None:
        if menu_id.isnumeric() and name.isalpha() and cost.isnumeric():
            c.execute('INSERT INTO menu_item (Menu_ID, Name, Cost) '
                      'VALUES (?,?,?)', (menu_id, name, cost))
            c.execute('COMMIT')
            c.execute('SELECT * FROM menu_item')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Menu Item")
    return render_template("data_invalid.html", field="Menu Item")


@app.route('/add_menu_item', methods=['GET'])
def add_menu_item_page():
    return render_template("add_menu_item.html")


@app.route('/display_menu_items', methods=['GET'])
def display_menu_items_page():
    header_row = "Menu Item ID, Menu ID, Name, Cost"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM menu_item')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Menu Items", header_row=header_row, all_rows=all_rows)


@app.route('/add_ordered_item', methods=['POST'])
def add_ordered_item():
    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    menu_item_id = request.form['menu_item_id']
    order_id = request.form['order_id']
    quantity = request.form['quantity']

    c.execute('SELECT Menu_Item_ID FROM menu_item WHERE Menu_Item_ID = {pk}'.format(pk=menu_item_id))
    row = c.fetchone()
    if row is not None:
        if menu_item_id.isnumeric() and order_id.isnumeric() and quantity.isnumeric():
            c.execute('INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity) '
                      'VALUES (?,?,?)', (menu_item_id, order_id, quantity))
            c.execute('COMMIT')
            c.execute('SELECT * FROM ordered_item')
            for row in c:
                print(row)
            return render_template("data_added.html", field="Ordered Item")
    return render_template("data_invalid.html", field="Ordered Item")


@app.route('/add_ordered_item', methods=['GET'])
def add_ordered_item_page():
    return render_template("add_ordered_item.html")


@app.route('/display_ordered_items', methods=['GET'])
def display_ordered_items_page():
    header_row = "Ordered Item ID, Menu Item ID, Order ID, Quantity"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM ordered_item')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Ordered Items", header_row=header_row, all_rows=all_rows)


if __name__ == "__main__":
    set_up_database()
    app.run(debug=True, host='0.0.0.0', port=8080)
