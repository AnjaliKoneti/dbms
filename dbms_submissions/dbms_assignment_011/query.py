Q1 = '''SELECT `actor`.id,fname,lname,gender FROM cast JOIN actor 
        ON pid = `actor`.id JOIN movie ON mid = `movie`.id 
        WHERE name LIKE 'Annie%';'''


Q2 = '''SELECT `movie`.id,name,rank,year FROM moviedirector JOIN director 
        ON did = `director`.id JOIN movie ON mid = `movie`.id 
        WHERE (fname = 'Biff' AND lname = 'Malibu') AND year IN (1999,1994,2003) 
        ORDER BY rank DESC,year ASC; '''
        

Q3 = '''SELECT year,COUNT(id) FROM movie GROUP BY year 
        HAVING AVG(rank) > (SELECT AVG(rank) FROM movie) ORDER BY year ASC;'''


Q4 = '''SELECT * FROM movie WHERE year = 2001 AND rank < (SELECT AVG(rank) 
        FROM movie WHERE year = 2001) ORDER BY rank DESC LIMIT 10;'''


#Q5 = "SELECT id,(SELECT COUNT(`actor`.id) FROM cast JOIN actor ON pid = `actor`.id WHERE mid = `movie`.id AND gender = 'F'),(SELECT COUNT(`actor`.id) FROM cast JOIN actor ON pid = `actor`.id WHERE mid = `movie`.id AND gender = 'M') FROM movie ORDER BY id ASC LIMIT 100;"


#Q5 = "SELECT `movie`.id,COUNT(f),COUNT(m) FROM cast JOIN actor ON pid = `actor`.id JOIN movie ON mid = `movie`.id WHERE GENDER = 'F' AS f OR GENDER='M' AS m GROUP BY id ORDER BY id ASC LIMIT 100;"


Q6 = '''SELECT DISTINCT pid FROM cast JOIN actor ON pid = `actor`.id JOIN movie 
        ON mid = `movie`.id GROUP BY pid,mid HAVING COUNT(DISTINCT role)>1 
        ORDER BY pid ASC LIMIT 100;'''


Q7 = "SELECT fname,COUNT(id) FROM director GROUP BY fname HAVING COUNT(fname)>1;"


Q8 = '''SELECT `director`.id,fname,lname FROM director 
        WHERE EXISTS (SELECT * FROM moviedirector JOIN cast 
        ON `moviedirector`.mid = `cast`.mid WHERE 
        `moviedirector`.did = `director`.id GROUP BY did,`moviedirector`.mid 
        HAVING COUNT(DISTINCT pid)>=100)
        
        AND NOT EXISTS(SELECT * FROM moviedirector JOIN cast 
        ON `moviedirector`.mid = `cast`.mid WHERE 
        `moviedirector`.did = `director`.id GROUP BY did,`moviedirector`.mid 
        HAVING COUNT(DISTINCT pid)<100);'''