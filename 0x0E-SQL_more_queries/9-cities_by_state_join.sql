-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, (
	SELECT name
	FROM states
	WHERE id = cities.states_id
)AS state_name FROM cities ORDER BY id ASC;
