-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
/* ANOTHER WAY TO DO IT.
	SELECT
	(
		SELECT tv_shows.title
		FROM tv_shows
		WHERE tv_shows.id = show_id
	) AS show_title, genre_id
	FROM tv_show_genres
	ORDER BY show_title, genre_id;
*/
SELECT tv_shows.title As title, genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = show_id
ORDER BY title, genre_id;
