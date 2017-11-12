-- ######################################################################## DROP
-- foreign keys
ALTER TABLE car_transaction DROP CONSTRAINT transaction_car;
ALTER TABLE car_transaction DROP CONSTRAINT transaction_client;
ALTER TABLE car_transaction DROP CONSTRAINT transaction_seller;

-- tables
DROP TABLE car;
DROP TABLE car_transaction;
DROP TABLE client;
DROP TABLE seller;

-- ######################################################################## CREATE
-- tables
-- Table: car
CREATE TABLE car (
    car_id number(8)  GENERATED BY DEFAULT ON NULL AS IDENTITY,
    car_brand varchar2(50)  NOT NULL,
    car_model varchar2(50)  NOT NULL,
    car_region varchar2(50)  NOT NULL,
    production_year number(4)  NOT NULL,
    mileage number(6)  NOT NULL,
    price number(6)  NOT NULL,
    engine_capacity number(4,2)  NOT NULL,
    engine_power number(3)  NOT NULL,
    gearbox_type varchar2(15)  NOT NULL,
    car_drive varchar2(10)  NOT NULL,
    car_body_color varchar2(15)  NOT NULL,
    car_body_type varchar2(15)  NOT NULL,
    car_cover varchar2(15)  NOT NULL,
    fuel_type varchar2(15)  NOT NULL,
    number_of_doors varchar2(5)  NOT NULL,
    CONSTRAINT car_pk PRIMARY KEY (car_id)
) ;

-- Table: car_transaction
CREATE TABLE car_transaction (
    transaction_id number(8)  GENERATED BY DEFAULT ON NULL AS IDENTITY,
    car_id number(8)  NOT NULL,
    client_id number(8)  NOT NULL,
    seller_id number(8)  NOT NULL,
    payment_type varchar2(20)  NOT NULL,
    transaction_date date  NOT NULL,
    CONSTRAINT car_transaction_pk PRIMARY KEY (transaction_id)
) ;

-- Table: client
CREATE TABLE client (
    client_id number(8)  GENERATED BY DEFAULT ON NULL AS IDENTITY,
    full_name varchar2(100)  NOT NULL,
    country varchar2(20)  NOT NULL,
    city varchar2(30)  NOT NULL,
    street varchar2(40)  NOT NULL,
    client_type varchar2(20)  NOT NULL,
    company_name varchar2(80)  NULL,
    CONSTRAINT client_pk PRIMARY KEY (client_id)
) ;

-- Table: seller
CREATE TABLE seller (
    seller_id number(8)  GENERATED BY DEFAULT ON NULL AS IDENTITY,
    full_name varchar2(100)  NOT NULL,
    country varchar2(20)  NOT NULL,
    city varchar2(20)  NOT NULL,
    street varchar2(30)  NOT NULL,
    seller_type varchar2(40)  NOT NULL,
    company_name varchar2(80)  NULL,
    CONSTRAINT seller_pk PRIMARY KEY (seller_id)
) ;

-- foreign keys
-- Reference: transaction_car (table: car_transaction)
ALTER TABLE car_transaction ADD CONSTRAINT transaction_car
    FOREIGN KEY (car_id)
    REFERENCES car (car_id) ON DELETE CASCADE;

-- Reference: transaction_client (table: car_transaction)
ALTER TABLE car_transaction ADD CONSTRAINT transaction_client
    FOREIGN KEY (client_id)
    REFERENCES client (client_id) ON DELETE CASCADE;

-- Reference: transaction_seller (table: car_transaction)
ALTER TABLE car_transaction ADD CONSTRAINT transaction_seller
    FOREIGN KEY (seller_id)
    REFERENCES seller (seller_id) ON DELETE CASCADE;

-- End of file.

