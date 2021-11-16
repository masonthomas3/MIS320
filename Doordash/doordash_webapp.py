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
    header_row = "Menu Item ID, Order ID, Quantity"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT * FROM ordered_item')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Ordered Items", header_row=header_row, all_rows=all_rows)


@app.route('/display_customer_driver_name', methods=['GET'])
def display_customer_driver_name_page():
    header_row = "Driver Name, Customer Name, Order ID"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT d.Name as Driver, c.Name as Customer, o.Order_ID ' +
              'FROM doordash_order o ' +
              'INNER JOIN driver d ' +
              'ON d.Driver_SSN = o.Driver_SSN ' +
              'INNER JOIN customer c ' +
              'ON c.Customer_ID = o.Customer_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Driver, Customer Names with Order ID",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_order_details', methods=['GET'])
def display_order_details():
    header_row = "Menu Item Name, Menu Item Cost, Order ID, Quantity"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT mi.Name as Menu_Item, mi.Cost, oi.Order_ID, oi.Quantity ' +
              'FROM menu_item mi ' +
              'INNER JOIN ordered_item oi ' +
              'ON mi.Menu_Item_ID = oi.Menu_Item_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Order Details",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_business_menus', methods=['GET'])
def display_business_menus():
    header_row = "Business, Menu, Menu Item, Item Cost"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT b.Name as Business, m.Name as Menu, mi.Name as Menu_Item, mi.Cost ' +
              'FROM business b ' +
              'INNER JOIN menu m ' +
              'ON b.Business_ID = m.Business_ID ' +
              'INNER JOIN menu_item mi ' +
              'ON m.Menu_ID = mi.Menu_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Business Menus",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_tips_given', methods=['GET'])
def display_tips_given():
    header_row = "Customer Name, Driver Name, Tip"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT c.Name AS Customer, d.Name AS Driver, dp.Tip '
              'FROM doordash_order o '
              'INNER JOIN payment p '
              'ON o.Payment_ID = p.Payment_ID '
              'INNER JOIN payment_method pm '
              'ON p.Payment_Method_ID = pm.Payment_Method_ID '
              'INNER JOIN customer c '
              'ON pm.Customer_ID = c.Customer_ID '
              'INNER JOIN driver_payment dp '
              'ON o.Driver_SSN = dp.Driver_SSN AND o.Order_ID = dp.Order_ID '
              'INNER JOIN driver d on dp.Driver_SSN = d.Driver_SSN')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Customer Tips",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_iowa_city_orders', methods=['GET'])
def display_iowa_city_orders():
    header_row = "Order ID, Customer Name"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT o.Order_ID, c.Name '
              'FROM doordash_order o '
              'INNER JOIN customer c '
              'ON o.Customer_ID = c.Customer_ID '
              'WHERE c.Address LIKE \'%Iowa City%\'')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Iowa City Orders",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_customer_driver_payments', methods=['GET'])
def display_customer_driver_payments():
    header_row = "Order ID, Payment Date, Customer, Customer Payment, Driver, Base_Pay, Tip"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT o.order_id, p.Payment_Date, c.Name as Customer, p.Amount as Customer_Payment, '
              'd.Name as Driver, dp.Base_Pay, dp.Tip '
              'FROM doordash_order o '
              'INNER JOIN payment p '
              'ON o.Payment_ID = p.Payment_ID '
              'INNER JOIN payment_method pm '
              'ON p.Payment_Method_ID = pm.Payment_Method_ID '
              'INNER JOIN customer c '
              'ON pm.Customer_ID = c.Customer_ID '
              'INNER JOIN driver_payment dp '
              'ON o.Driver_SSN = dp.Driver_SSN AND o.Order_ID = dp.Order_ID '
              'INNER JOIN driver d '
              'ON dp.Driver_SSN = d.Driver_SSN '
              'GROUP BY o.order_id, p.payment_date, c.name, p.amount, d.name, dp.base_pay, dp.tip '
              'ORDER BY o.order_id')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Customer/Driver Payments",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_driver_vehicles', methods=['GET'])
def display_driver_vehicles():
    header_row = "Driver, Make, Model, License Plate"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT d.Name, v.Make, v.Model, v.License_Plate '
              'FROM driver d '
              'INNER JOIN vehicle v '
              'ON d.Driver_SSN = v.Driver_SSN')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Driver Vehicles",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_driver_ratings', methods=['GET'])
def display_driver_ratings():
    header_row = "Name, Acceptance Rate, Completion Rate, On Time Rate, Customer Rating, Lifetime Deliveries"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT Name, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries '
              'FROM driver')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Driver Ratings",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_business_orders', methods=['GET'])
def display_business_orders():
    header_row = "Order ID, Business, Location, Delivery_Fee"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT o.Order_ID, b.Name, b.Location, b.Delivery_Fee '
              'FROM doordash_order o '
              'INNER JOIN ordered_item oi '
              'ON o.Order_ID = oi.Order_ID '
              'INNER JOIN menu_item mi '
              'ON oi.Menu_Item_ID = mi.Menu_Item_ID '
              'INNER JOIN menu m '
              'ON mi.Menu_ID = m.Menu_ID '
              'INNER JOIN business b '
              'ON m.Business_ID = b.Business_ID '
              'GROUP BY o.Order_ID, b.Name, b.Location, b.Delivery_Fee '
              'ORDER BY o.Order_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Business Orders",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_amount_paid', methods=['GET'])
def display_amount_paid():
    header_row = "Customer, Payment Method ID, Total Amount Paid"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT c.Name, pm.Payment_Method_ID, sum(p.Amount) AS Total '
              'FROM customer c '
              'INNER JOIN payment_method pm '
              'ON c.Customer_ID = pm.Customer_ID '
              'INNER JOIN payment p '
              'ON pm.Payment_Method_ID = p.Payment_Method_ID '
              'GROUP BY c.Name, pm.Payment_Method_ID '
              'ORDER BY pm.Payment_Method_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Customer's Total Amount Paid",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_driver_total_compensation', methods=['GET'])
def display_driver_total_compensation():
    header_row = "Driver, Total Base Pay, Total Tips, Total Payment"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT d.Name, SUM(dp.Base_Pay), SUM(dp.Tip), SUM(dp.Base_Pay) + SUM(dp.Tip) AS Total_Payment '
              'FROM driver d '
              'INNER JOIN driver_payment dp '
              'ON d.Driver_SSN = dp.Driver_SSN '
              'GROUP BY d.Name '
              'ORDER BY Total_Payment desc')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Driver's Total Compensation",
                           header_row=header_row, all_rows=all_rows)


@app.route('/display_customer_order_locations', methods=['GET'])
def display_customer_order_locations():
    header_row = "Order ID, Customer, Business Location"

    sqlite_file = 'doordash_db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT DISTINCT o.Order_ID, c.Name, b.Location '
              'FROM doordash_order o '
              'INNER JOIN customer c '
              'ON o.Customer_ID = c.Customer_ID '
              'INNER JOIN ordered_item oi '
              'ON o.Order_ID = oi.Order_ID '
              'INNER JOIN menu_item mi '
              'ON oi.Menu_Item_ID = mi.Menu_Item_ID '
              'INNER JOIN menu m '
              'ON mi.Menu_ID = m.Menu_ID '
              'INNER JOIN business b '
              'ON m.Business_ID = b.Business_ID '
              'ORDER BY o.Order_ID')
    all_rows = c.fetchall()

    return render_template("display_data.html", field="Customer Order Locations",
                           header_row=header_row, all_rows=all_rows)


if __name__ == "__main__":
    set_up_database()
    app.run(debug=True, host='0.0.0.0', port=8080)
