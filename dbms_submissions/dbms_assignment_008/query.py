Q1 = "SELECT director.id,director.fname FROM director WHERE EXISTS(SELECT director.id FROM moviedirector JOIN movie ON moviedirector.mid = movie.id WHERE moviedirector.did = director.id AND year > 2000) AND NOT EXISTS(SELECT director.id FROM moviedirector JOIN movie ON moviedirector.mid = movie.id WHERE moviedirector.did = director.id AND year < 2000) ORDER BY director.id ASC;"
Q2 = "SELECT fname,(SELECT name  FROM moviedirector  JOIN movie on moviedirector.mid = movie.id WHERE moviedirector.did = director.id  ORDER BY rank DESC,name ASC LIMIT 1) FROM director LIMIT 100;"  

Q3 = "SELECT * FROM actor WHERE NOT EXISTS (SELECT `cast`.pid FROM cast JOIN movie ON `cast`.mid = `movie`.id WHERE `cast`.pid = `actor`.id AND year BETWEEN 1990 AND 2000) ORDER BY `actor`.id DESC LIMIT 100;"
