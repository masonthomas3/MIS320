BEGIN TRANSACTION;
DROP TABLE IF EXISTS "driver";
CREATE TABLE IF NOT EXISTS "driver" (
	"Driver_SSN"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Acceptance_Rate"	REAL NOT NULL DEFAULT 0.0,
	"Completion_Rate"	REAL NOT NULL DEFAULT 0.0,
	"Customer_Rating"	REAL NOT NULL DEFAULT 0,
	"On_Time_Rate"	REAL NOT NULL DEFAULT 0.0,
	"Lifetime_Deliveries"	INTEGER NOT NULL DEFAULT 0,
	"Age"	INTEGER NOT NULL,
	PRIMARY KEY("Driver_SSN")
);
DROP TABLE IF EXISTS "customer";
CREATE TABLE IF NOT EXISTS "customer" (
	"Customer_ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Phone_Number"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Address"	TEXT NOT NULL,
	PRIMARY KEY("Customer_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "doordash_order";
CREATE TABLE IF NOT EXISTS "doordash_order" (
	"Order_ID" INTEGER NOT NULL,
	"Driver_SSN"	INTEGER NOT NULL,
	"Customer_ID"	INTEGER NOT NULL,
	"Payment_ID"	INTEGER NOT NULL,
	FOREIGN KEY("Customer_ID") REFERENCES "customer"("Customer_ID"),
	FOREIGN KEY("Driver_SSN") REFERENCES "driver"("Driver_SSN"),
	FOREIGN KEY("Payment_ID") REFERENCES "payment"("Payment_ID"),
	PRIMARY KEY("Order_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "driver_payment";
CREATE TABLE IF NOT EXISTS "driver_payment" (
	"Driver_SSN"	INTEGER NOT NULL,
	"Order_ID"	INTEGER NOT NULL,
	"Base_Pay"	REAL NOT NULL DEFAULT 3.00,
	"Tip"	REAL NOT NULL DEFAULT 0.00,
	FOREIGN KEY("Order_ID") REFERENCES "doordash_order",
	FOREIGN KEY("Driver_SSN") REFERENCES "driver"("Driver_SSN"),
	PRIMARY KEY("Driver_SSN","Order_ID")
);
DROP TABLE IF EXISTS "business";
CREATE TABLE IF NOT EXISTS "business" (
	"Business_ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Location"	TEXT NOT NULL,
	"Delivery_Fee"	REAL NOT NULL DEFAULT 0.00,
	PRIMARY KEY("Business_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "menu";
CREATE TABLE IF NOT EXISTS "menu" (
	"Menu_ID"	INTEGER NOT NULL,
	"Business_ID"	INTEGER NOT NULL,
	"Name"	TEXT,
	"Description"	TEXT,
	FOREIGN KEY("Business_ID") REFERENCES "business"("Business_ID"),
	PRIMARY KEY("Menu_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "menu_item";
CREATE TABLE IF NOT EXISTS "menu_item" (
	"Menu_Item_ID"	INTEGER NOT NULL,
	"Menu_ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Cost"	REAL NOT NULL DEFAULT 0.00,
	FOREIGN KEY("Menu_ID") REFERENCES "menu"("Menu_ID"),
	PRIMARY KEY("Menu_Item_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "ordered_item";
CREATE TABLE IF NOT EXISTS "ordered_item" (
	"Menu_Item_ID"	INTEGER NOT NULL,
	"Order_ID"	INTEGER NOT NULL,
	"Quantity"	TEXT NOT NULL DEFAULT 1,
	FOREIGN KEY("Menu_Item_ID") REFERENCES "menu_item"("Menu_Item_ID"),
	FOREIGN KEY("Order_ID") REFERENCES "doordash_order",
	PRIMARY KEY("Menu_Item_ID","Order_ID")
);
DROP TABLE IF EXISTS "vehicle";
CREATE TABLE IF NOT EXISTS "vehicle" (
	"Vehicle_ID"	INTEGER NOT NULL,
	"Driver_SSN"	INTEGER NOT NULL,
	"Make"	TEXT NOT NULL,
	"License_Plate"	TEXT NOT NULL,
	"Model"	TEXT NOT NULL,
	FOREIGN KEY("Driver_SSN") REFERENCES "driver"("Driver_SSN"),
	PRIMARY KEY("Vehicle_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "payment_method";
CREATE TABLE IF NOT EXISTS "payment_method" (
	"Payment_Method_ID"	INTEGER NOT NULL,
	"Customer_ID"	INTEGER NOT NULL,
	"Card_Number"	INTEGER NOT NULL,
	"Expiration_Date"	TEXT NOT NULL,
	"Security_Number"	INTEGER NOT NULL,
	FOREIGN KEY("Customer_ID") REFERENCES "customer"("Customer_ID"),
	PRIMARY KEY("Payment_Method_ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "payment";
CREATE TABLE IF NOT EXISTS "payment" (
	"Payment_ID"	INTEGER NOT NULL,
	"Payment_Method_ID"	INTEGER NOT NULL,
	"Amount"	REAL NOT NULL DEFAULT 0.00,
	"Date"	TEXT NOT NULL,
	FOREIGN KEY("Payment_Method_ID") REFERENCES "payment_method"("Payment_Method_ID"),
	PRIMARY KEY("Payment_ID" AUTOINCREMENT)
);

INSERT INTO customer (Customer_ID, Name, Phone_Number, Email, Address)
VALUES (15000, "Mason Thomas", "5152916827", "mthomas3@iastate.edu", "812 Cove Dr. Ames, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Jack Roger", "5152316882", "jroger@iastate.edu", "200 Ash Dr. Ames, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Grant Stephens", "3192689128", "gstephens@iastate.edu", "381 Maple Ave. Ames, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Matt Lyle", "3097628712", "mlyle@iastate.edu", "8234 Ash Ave. Ames, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Riley Beyer", "3098320321", "rbeyer@iastate.edu", "122 Beach Rd. Ames, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Patricia Turner", "9843249021", "pturner@uiowa.edu", "342 Grove Dr. Iowa City, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Madison Rider", "9418430231", "mrider@uiowa.edu", "7432 Florida Rd. Iowa City, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Michael James", "3094120312", "mjames@uiowa.edu", "2341 Ontario Dr. Iowa City, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Sue Snyder", "6548120129", "ssnyder@gmail.com", "1312 110th St. Carroll, IA");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Patrick Jordan", "8417823911", "pjordan@uiowa.edu", "9201 50th St. Iowa City, IA");



INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (234742743, "Ryan Lawrence", 23);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (209372747, "Patrick Carter", 23);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (982735476, "Michael Brady", 45);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (453728938, "Jon Reid", 39);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (837263748, "Hailee Gustafson", 18);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (872635419, "Teresa Jones", 42);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (871627384, "Theresa Judon", 27);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (653819732, "Marcus Gilmore", 22);

INSERT INTO driver (Driver_SSN, Name, Age)
VALUES (281374921, "Reed Selby", 57);



INSERT INTO business (Business_ID, Name, Location, Delivery_Fee)
VALUES (40000, "McDonalds", "Ames, IA", 2.95);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Chick-Fil-A", "Des Moines, IA", 1.99);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Dairy Queen", "Story City, IA", 0.00);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Culver's", "Iowa City", 3.50);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Burger King", "Ames, IA", 2.95);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Red Robin", "Des Moines, IA", 4.00);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Perkins", "Iowa City, IA", 2.95);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("McDonalds", "Iowa City, IA", 2.95);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Coldstone Creamery", "Ames, IA", 3.30);

INSERT INTO business (Name, Location, Delivery_Fee)
VALUES ("Buffalo Wild Wings", "Ames, IA", 4.25);



INSERT INTO menu (Menu_ID, Business_ID, Name, Description)
VALUES (45000, 40000, "Lunch", "This is the lunch menu that runs from 11am to 4pm");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40000, "Breakfast", "This is the breakfast menu that runs from 8am to 11am");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40001, "Lunch", "This is the lunch menu that runs from 11am to 2pm");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40001, "Dinner", "This is the dinner menu that runs from 2pm to 9pm");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40002, "All Day", "This is the menu that runs all day");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40003, "Ice Cream Menu", "This is the ice cream menu that runs all day");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40004, "Lunch", "This is the lunch menu that runs from 10am to 3pm");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40005, "Dessert", "This is the dessert menu that runs from 2pm to 10pm");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40006, "Breakfast", "This is the breakfast menu that runs all day");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40007, "Lunch", "This is the lunch menu that runs from 10am to close");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40008, "Ice Cream", "This is the ice cream menu that runs all day");

INSERT INTO menu (Business_ID, Name, Description)
VALUES (40009, "Dinner", "This is the dinner menu that runs from 4pm to midnight");



INSERT INTO payment_method (Payment_Method_ID, Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (25000, 15000, 1234567891234567, "02/22", 304);

INSERT INTO payment (Payment_ID, Payment_Method_ID, Amount, Date)
VALUES (30000, 25000, 13.50, "11-Nov-2021");

INSERT INTO vehicle (Vehicle_ID, Driver_SSN, Make, License_Plate, Model)
VALUES (15000, 234742743, "Honda", "B4SKM9", "CRV");

INSERT INTO menu_item (Menu_Item_ID, Menu_ID, Name, Cost)
VALUES (50000, 45000, "McChicken", 1.00);

INSERT INTO doordash_order (Order_ID, Driver_SSN, Customer_ID, Payment_ID)
VALUES (35000, 234742743, 15000, 30000);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50000, 35000, 2);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (23474, 35000, 3.50, 2.50);

COMMIT;
