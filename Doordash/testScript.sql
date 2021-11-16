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
	"Model"	TEXT NOT NULL,
	"License_Plate"	TEXT NOT NULL,
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
	"Payment_Date"	TEXT NOT NULL,
	FOREIGN KEY("Payment_Method_ID") REFERENCES "payment_method"("Payment_Method_ID"),
	PRIMARY KEY("Payment_ID" AUTOINCREMENT)
);

INSERT INTO customer (Customer_ID, Name, Phone_Number, Email, Address)
VALUES (20000, "Brian Clubine", "5152316827", "bclubine@iastate.edu", "812 Cove Dr. Ames, IA");

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


INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (234742743, 'Ryan Lawrence', 23, 78.5, 92, 62, 5, 140 );

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (209372747, 'Patrick Carter', 23, 90.3, 98, 84, 3.2, 100);

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (982735476, 'Michael Brady', 45,75.9, 87, 97, 4.2, 203);

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (453728938, 'Jon Reid', 39, 60, 99, 62, 4.4, 34 );

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (837263748, 'Hailee Gustafson', 18, 79, 92, 94, 3.5, 134);

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (872635419, 'Teresa Jones', 42, 89.5, 92.2, 79.1, 2.3, 256);

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (871627384, 'Theresa Judon', 27, 80.9, 97, 89.4, 1.1, 89);

INSERT INTO driver (Driver_SSN, Name, Age, Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (653819732, 'Marcus Gilmore', 22,  69.2, 80.9, 65.7, 4.6, 101);

INSERT INTO driver (Driver_SSN, Name, Age,Acceptance_Rate, Completion_Rate, On_Time_Rate, Customer_Rating, Lifetime_Deliveries)
VALUES (281374921, 'Reed Selby', 57, 70.6, 93, 89.9, 3.1, 145);



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

--01
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40000, "Breakfast", "This is the breakfast menu that runs from 8am to 11am");

--02
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40001, "Lunch", "This is the lunch menu that runs from 11am to 2pm");

--03
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40001, "Dinner", "This is the dinner menu that runs from 2pm to 9pm");

--04
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40002, "All Day", "This is the menu that runs all day");

--05
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40003, "Ice Cream Menu", "This is the ice cream menu that runs all day");

--06
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40004, "Lunch", "This is the lunch menu that runs from 10am to 3pm");

--07
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40005, "Dessert", "This is the dessert menu that runs from 2pm to 10pm");

--08
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40006, "Breakfast", "This is the breakfast menu that runs all day");

--09
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40007, "Lunch", "This is the lunch menu that runs from 10am to close");

--10
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40008, "Ice Cream", "This is the ice cream menu that runs all day");

--11
INSERT INTO menu (Business_ID, Name, Description)
VALUES (40009, "Dinner", "This is the dinner menu that runs from 4pm to midnight");


INSERT INTO payment_method (Payment_Method_ID, Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (25000, 20000, 1234567891234567, "02/22", 304);

--01
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20001, 8738293847192384, "09/25", 928);

--02
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20001, 7634749509123847, "12/21", 721);

--03
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20002, 1232398768894736, "10/22", 834);

--04
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20003, 7434829039212345, "04/23", 314);

--05
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20004, 5462816232389430, "01/24", 412);

--06
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20005, 8372912389123740, "06/25", 342);

--07
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20006, 9431074127401284, "12/23", 841);

--08
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20007, 5203850385038502, "02/23", 842);

--09
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20008, 5802854012840128, "01/27", 311);

--10
INSERT INTO payment_method (Customer_ID, Card_Number, Expiration_Date, Security_Number)
VALUES (20009, 4081248024810840, "02/24", 283);

INSERT INTO payment (Payment_ID, Payment_Method_ID, Amount, Payment_Date)
VALUES (30000, 25000, 13.50, "11-Nov-2021");

--01
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25000, 22.75, "15-Nov-2021");

--02
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25001, 17.75, "12-Oct-2021");

--03
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25002, 33.81, "30-Oct-2021");

--04
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25003, 21.23, "30-Sep-2021");

--05
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25004, 12.11, "22-Oct-2021");

--06
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25005, 42.21, "21-Aug-2021");

--07
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25006, 08.50, "30-Mar-2021");

--08
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25007, 26.72, "04-Nov-2021");

--09
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25008, 80.31, "10-Nov-2021");

--10
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25009, 10.90, "01-Nov-2021");

--11
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25010, 22.22, "04-Oct-2021");

--12
INSERT INTO payment (Payment_Method_ID, Amount, Payment_Date)
VALUES (25010, 19.87, "04-Nov-2021");

INSERT INTO vehicle (Vehicle_ID, Driver_SSN, Make, Model, License_Plate)
VALUES (15000, 234742743, "Honda", "CRV", "B4SKM9");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (209372747, "Ford", "Fusion", "HYW062");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (982735476, "Toyota", "Camry", "XYZ438");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (453728938, "Subaru", "Outback", "OAS812");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (837263748, "BMW", "I8", "KAS012");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (872635419, "Toyota", "Tacoma", "MAS921");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (871627384, "Buick", "Century", "ERA763");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (653819732, "Buick", "Park Avenue", "URS843");

INSERT INTO vehicle (Driver_SSN, Make, Model, License_Plate)
VALUES (281374921, "Chevy", "Silverado", "HFE453");

INSERT INTO menu_item (Menu_Item_ID, Menu_ID, Name, Cost)
VALUES (50000, 45000, "McChicken", 1.00);

--01
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45000, "McFlurry", 2.05);

--02
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45001, "Egg McMuffin", 3.50);

--03
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45001, "McGriddle", 3.39);

--04
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45002, "Chicken Nuggets (8 piece)", 4.50);

--05
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45002, "Chicken Sandwich Meal", 7.95);

--06
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45003, "Chicken Sandwich Meal", 7.95);

--07
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45004, "Small M&M Blizzard", 3.30);

--08
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45004, "Medium M&M Blizzard", 4.30);

--09
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45004, "Large M&M Blizzard", 5.30);

--10
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45004, "Cheeseburger Meal", 6.69);

--11
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45005, "Small Chocolate Concrete Mixer", 3.19);

--12
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45005, "Medium Chocolate Concrete Mixer", 4.19);

--13
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45006, "Whopper Meal", 8.80);

--14
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45006, "Chicken Fries", 2.00);

--15
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45007, "Chocolate Milkshake", 4.00);

--16
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45007, "Lava Cake", 4.50);

--17
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45008, "Buttermilk Pancake Short Stack", 7.99);

--18
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45008, "Belgian Waffle Platter", 13.19);

--19
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45009, "McChicken", 2.00);

--20
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45010, "Like It Chocolate Devotion", 7.79);

--21
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45010, "Love It Chocolate Devotion", 8.49);

--22
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45010, "Gotta Have It Chocolate Devotion", 10.39);

--23
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45011, "6 Boneless Wings", 8.99);

--24
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45011, "10 Boneless Wings", 12.49);

--25
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45011, "15 Boneless Wings", 17.79);

--26
INSERT INTO menu_item (Menu_ID, Name, Cost)
VALUES (45011, "20 Boneless Wings", 21.99);

INSERT INTO doordash_order (Order_ID, Driver_SSN, Customer_ID, Payment_ID)
VALUES (35000, 234742743, 20000, 30000);

--01
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (234742743, 20000, 30001);

--02
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (209372747, 20000, 30002);

--03
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (982735476, 20001, 30003);

--04
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (453728938, 20002, 30004);

--05
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (837263748, 20003, 30005);

--06
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (872635419, 20004, 30006);

--07
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (871627384, 20005, 30007);

--08
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (871627384, 20006, 30008);

--09
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (653819732, 20007, 30009);

--10
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (281374921, 20008, 30010);

--11
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (281374921, 20009, 30011);

--12
INSERT INTO doordash_order (Driver_SSN, Customer_ID, Payment_ID)
VALUES (281374921, 20009, 30012);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50000, 35000, 2);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50001, 35000, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50002, 35001, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50003, 35001, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50004, 35002, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50005, 35002, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50006, 35003, 2);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50007, 35004, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50008, 35004, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50009, 35004, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50010, 35005, 3);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50011, 35006, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50012, 35006, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50013, 35007, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50014, 35007, 3);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50015, 35008, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50016, 35008, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50017, 35009, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50018, 35009, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50019, 35010, 4);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50022, 35011, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50024, 35012, 1);

INSERT INTO ordered_item (Menu_Item_ID, Order_ID, Quantity)
VALUES (50026, 35012, 1);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (234742743, 35000, 3.50, 2.50);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (234742743, 35001, 4.00, 2.50);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (209372747, 35002, 4.25, 2.50);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (982735476, 35003, 3.00, 4.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (453728938, 35004, 3.00, 2.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (837263748, 35005, 5.00, 5.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (872635419, 35006, 5.00, 0.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (871627384, 35007, 8.00, 1.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (871627384, 35008, 2.00, 5.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (653819732, 35009, 4.00, 5.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (281374921, 35010, 2.00, 4.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (281374921, 35011, 5.00, 4.00);

INSERT INTO driver_payment (Driver_SSN, Order_ID, Base_Pay, Tip)
VALUES (281374921, 35012, 5.00, 5.00);

COMMIT;
