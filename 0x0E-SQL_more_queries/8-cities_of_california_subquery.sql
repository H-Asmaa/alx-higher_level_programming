-- A script that creates the database hbtn_0d_usa and the table cities.
SELECT id, name
FROM cities WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
)ORDER BY id ASC;
