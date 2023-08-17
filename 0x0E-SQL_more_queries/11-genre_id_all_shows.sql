-- A script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT title, IFNULL(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = id
ORDER BY title, tv_show_genres.genre_id;
