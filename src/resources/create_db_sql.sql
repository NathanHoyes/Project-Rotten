DROP DATABASE IF EXISTS Rotten_Test_Database;
CREATE DATABASE Rotten_Test_Database;
USE Rotten_Test_Database;

CREATE TABLE Logins (
    LoginID int AUTO_INCREMENT,
    LoginTokenHash VARCHAR(256) NOT NULL,
    HashedEmail VARCHAR(256) NOT NULL,
    PRIMARY KEY(LoginID)
);

CREATE TABLE Locations (
    LocationID int AUTO_INCREMENT,
    LocationName VARCHAR(256) NOT NULL,
    PRIMARY KEY(LocationID)
);

CREATE TABLE PrimaryProductCategory (
    PrimaryProductCategoryID int AUTO_INCREMENT,
    PrimaryProductCategoryName VARCHAR(256) NOT NULL,
    PRIMARY KEY(PrimaryProductCategoryID)
);

CREATE TABLE SecondaryProductCategory (
    SecondaryProductCategoryID int AUTO_INCREMENT,
    SecondaryProductCategoryName VARCHAR(256) NOT NULL,
    PRIMARY KEY(SecondaryProductCategoryID)
);

CREATE TABLE Products (
    ProductID int AUTO_INCREMENT,
    ProductName VARCHAR(256) NOT NULL,
    PrimaryProductCategoryID int,
    SecondaryProductCategoryID int,
    UnitCostPence int,
    UnitWeightGrams int,
    FOREIGN KEY (PrimaryProductCategoryID) REFERENCES PrimaryProductCategory(PrimaryProductCategoryID),
    FOREIGN KEY (SecondaryProductCategoryID) REFERENCES SecondaryProductCategory(SecondaryProductCategoryID),
    PRIMARY KEY(ProductID)
);


CREATE TABLE Staff (
    StaffID int AUTO_INCREMENT,
    LoginID int,
    FirstName Varchar(32) NOT NULL,
    LastName Varchar(32) NOT NULL,
    LocationID int,
    FOREIGN KEY (LoginID) REFERENCES Logins(LoginID),
    FOREIGN KEY(LocationID) REFERENCES Locations(LocationID),
    PRIMARY KEY(StaffID)
);

CREATE TABLE Admin (
    AdminID int AUTO_INCREMENT,
    StaffID int,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID),
    PRIMARY KEY(AdminID)
);

CREATE TABLE Wastage (
    WasteID int AUTO_INCREMENT,
    ProductID int,
    Quantity float NOT NULL,
    StaffID int,
    LocationID int,
    DateTimeRecorded DATETIME,
    FOREIGN KEY (ProductId) REFERENCES Products(ProductID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
    PRIMARY KEY(WasteID)
);

-- add values here, will need to add several rows for each
INSERT INTO Logins(LoginTokenHash,HashedEmail) VALUES("testHash","testEmail");
INSERT INTO Logins(LoginTokenHash,HashedEmail) VALUES("f359e5ce5ee865e2448c07b69906c99bd3ae0fea22968088174a7eda5ba1dfaa","fdd8157ddd7d2ade12a3799aa9998a8de76d291c1f3ddce3b3bb7edb2f42c7a8");
INSERT INTO Logins(LoginTokenHash,HashedEmail) VALUES("ac1c320ba378f55c2e246806ea91a4b7c78f2b875f135b6ab7a4c163bcab76e1","efb94aa4fd0ee88a727cc52515e4410a18f2f59bb5464e7c3114b6290b89a775");

INSERT INTO Locations(LocationName) VALUES("The Frog and Dog");
INSERT INTO Locations(LocationName) VALUES("The Cat and Bat");
INSERT INTO Locations(LocationName) VALUES("The Pig and Fig");
INSERT INTO Locations(LocationName) VALUES("Testaraunt");

INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Meat");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Vegetables");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Dairy");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Chilled");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Fruit");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Prepared Foods");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Desserts");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Dry Goods");
INSERT INTO PrimaryProductCategory(PrimaryProductCategoryName) VALUES("Other");

INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Red Meat");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("White Meat");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Fish");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Bread");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Cakes");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Ice Cream");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Soup");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Sauce");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Pastries");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Cakes");
INSERT INTO SecondaryProductCategory(SecondaryProductCategoryName) VALUES("Other");

-- Name, primary category id, secondary id, unit cost (pence)
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Chicken Breast", 1, 2, 500, 220);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Fillet Steak", 1, 1, 1200, 280);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Apple", 6, 10, 80, 60);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Milk", 1, 2, 160, 2000);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Salmon", 1, 3, 700, 180);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Trout", 1, 3, 750, 220);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Sirloin", 1, 2, 1100, 300);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Beef Patty", 1, 2, 500, 120);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Bernaise", 6, 8, 50, 50);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Vanilla Ice Cream", 4, 6, 1500, 1000);
INSERT INTO Products(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) VALUES("Pasta", 8, 11, 500, 500);

INSERT INTO Staff(LoginID, FirstName, LastName, LocationID) VALUES(1,"Andrew", "Stevens", 1);
INSERT INTO Staff(LoginID, FirstName, LastName, LocationID) VALUES(1,"Nathan", "Hoyes", 2);
INSERT INTO Staff(LoginID, FirstName, LastName, LocationID) VALUES(1,"Chuck", "McFucks", 3);

INSERT INTO Admin(StaffID) VALUES(1);
INSERT INTO Admin(StaffID) VALUES(2);

-- ProductId, Amount, DateTime, StaffId, LocationId
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(1, 2, "2023-01-30 20:00:00", 1, 1);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(2, 4, "2023-01-30 20:10:00", 1, 1);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(4, 3, "2023-01-30 20:15:00", 1, 1);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(1, 2, "2023-01-30 20:00:00", 2, 3);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(2, 4, "2023-01-30 20:10:00", 2, 3);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(4, 3, "2023-01-30 20:15:00", 2, 3);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(11, 2, "2023-01-30 21:00:00", 3, 2);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(7, 4, "2023-01-30 21:10:00", 3, 2);
INSERT INTO Wastage(ProductID, Quantity, DateTimeRecorded, StaffID, LocationID) VALUES(6, 3, "2023-01-30 22:15:00", 3, 2);
