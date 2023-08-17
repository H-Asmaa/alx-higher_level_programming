-- A  script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title ASC, tv_show_genres.genre_id ASC;
