-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY
    tv_shows.title,
    tv_show_genres.genre_id;