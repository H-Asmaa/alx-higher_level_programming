-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title As title, genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = show_id
ORDER BY title, genre_id;
