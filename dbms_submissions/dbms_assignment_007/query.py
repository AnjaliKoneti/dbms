Q1 = "SELECT COUNT(id) FROM movie WHERE year < 2000;"
Q2 = "SELECT AVG(rank) FROM movie WHERE year = 1991;"
Q3 = "SELECT MIN(rank) FROM movie WHERE year = 1991;"
Q4 = "SELECT fname,lname FROM cast INNER JOIN actor ON pid = id WHERE mid = 27;"
Q5 = "SELECT COUNT(mid) FROM cast INNER JOIN actor ON pid = id WHERE fname = 'Jon' AND lname = 'Dough';"
Q6 = "SELECT DISTINCT name FROM cast JOIN movie ON mid = id WHERE (name LIKE 'Young Latin Girls%') AND (year BETWEEN 2003 AND 2006);"
Q7 = "SELECT DISTINCT fname,lname FROM ((moviedirector INNER JOIN director ON did = `director`.id)INNER JOIN movie ON `moviedirector`.mid = `movie`.id)  WHERE name LIKE 'Star Trek%';"
Q8 = "SELECT name FROM moviedirector JOIN director ON `moviedirector`.did = `director`.id JOIN cast ON `moviedirector`.mid = `cast`.mid JOIN movie ON `cast`.mid = `movie`.id JOIN actor ON `cast`.pid = `actor`.id WHERE (`director`.fname = 'Jackie (I)' AND `director`.lname = 'Chan' ) AND (`actor`.fname = 'Jackie (I)' AND `actor`.lname = 'Chan') ORDER BY name ASC"
Q9 = "SELECT fname,lname FROM ((moviedirector INNER JOIN director ON did = `director`.id)INNER JOIN movie ON mid = `movie`.id)WHERE year = 2001 GROUP BY `director`.id HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;"
Q10 = "SELECT GENDER,COUNT(id) FROM actor GROUP BY gender;"
Q11 = "SELECT DISTINCT m.name,n.name,m.rank,m.year FROM (movie m INNER JOIN movie n ON (m.name != n.name AND m.year = n.year AND m.rank = n.rank)) ORDER BY m.name ASC LIMIT 100;"
Q12 = "SELECT fname,year,AVG(rank) FROM cast INNER JOIN actor ON `cast`.pid = `actor`.id INNER JOIN movie ON `cast`.mid = `movie`.id GROUP BY `actor`.id,year ORDER BY fname ASC,year DESC LIMIT 100;"
Q13 = '''SELECT `actor`.fname,`director`.fname,AVG(rank) AS score FROM moviedirector 
    JOIN director ON `moviedirector`.did = `director`.id JOIN cast ON 
    `moviedirector`.mid = `cast`.mid JOIN movie ON `cast`.mid = `movie`.id JOIN actor ON
    `cast`.pid = `actor`.id GROUP BY `actor`.id,`director`.id HAVING 
    COUNT(`moviedirector`.mid)>=5 ORDER BY score DESC,`director`.fname ASC,
    `actor`.fname DESC LIMIT 100;'''