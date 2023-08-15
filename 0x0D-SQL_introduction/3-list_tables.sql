-- A script that lists all the tables of a database in the non-interractive mode.
SET @db = ?;
USE @db;
SHOW TABLES;
