-- A script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = id
ORDER BY title ASC, tv_show_genres.genre_id ASC;
