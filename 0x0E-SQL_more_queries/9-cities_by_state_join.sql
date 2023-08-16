-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, (
	SELECT states.name
	FROM states
	WHERE states.id = cities.states_id
)AS state_name FROM cities ORDER BY id ASC;
