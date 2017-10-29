-- foreign keys
ALTER TABLE car_features DROP CONSTRAINT car_features_car;
ALTER TABLE car_transaction DROP CONSTRAINT transaction_car;
ALTER TABLE car_transaction DROP CONSTRAINT transaction_client;
ALTER TABLE car_transaction DROP CONSTRAINT transaction_seller;

-- tables
DROP TABLE car;
DROP TABLE car_features;
DROP TABLE car_transaction;
DROP TABLE client;
DROP TABLE seller;

-- End of file.

