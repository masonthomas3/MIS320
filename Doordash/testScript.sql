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
DROP TABLE IF EXISTS "order";
CREATE TABLE IF NOT EXISTS "order" (
	"Driver_SSN"	INTEGER NOT NULL,
	"Customer_ID"	INTEGER NOT NULL,
	"Payment_ID"	INTEGER NOT NULL,
	FOREIGN KEY("Customer_ID") REFERENCES "customer"("Customer_ID"),
	FOREIGN KEY("Driver_SSN") REFERENCES "driver"("Driver_SSN"),
	FOREIGN KEY("Payment_ID") REFERENCES "payment"("Payment_ID"),
	PRIMARY KEY("Driver_SSN","Customer_ID","Payment_ID")
);
DROP TABLE IF EXISTS "driver_payment";
CREATE TABLE IF NOT EXISTS "driver_payment" (
	"Driver_SSN"	INTEGER NOT NULL,
	"Order_ID"	INTEGER NOT NULL,
	"Base_Pay"	REAL NOT NULL DEFAULT 3.00,
	"Tip"	REAL NOT NULL DEFAULT 0.00,
	FOREIGN KEY("Order_ID") REFERENCES "order",
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
	FOREIGN KEY("Order_ID") REFERENCES "order",
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

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Mason Thomas", "515-291-6827", "mthomas3@iastate.edu", "812 Cove Dr. Ames, IA 50010");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Jack Roger", "515-231-6882", "jroger@iastate.edu", "200 Ash Dr. Ames, IA 50010");

INSERT INTO customer (Name, Phone_Number, Email, Address)
VALUES ("Grant Stephens", "319-268-9128", "gstephens@iastate.edu", "381 Maple Ave. Ames, IA 50010");

COMMIT;
