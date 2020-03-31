-- Creates the "hbnb_dev_db" database with the user "hbnb_dev" in the localhost.
-- The password for the that user will be "hbnb_dev_pwd" and have all privileges
-- on this database. The user has only SELECT privileges on the database called
-- "performance_schema".

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
