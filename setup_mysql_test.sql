-- Creates the "hbnb_test_db" database with the user "hbnb_test" in localhost.
-- The password for the that user will be "hbnb_test_pwd" and have all
-- privileges on this database. The user has only SELECT privileges on the
-- database called "performance_schema".

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;


CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
