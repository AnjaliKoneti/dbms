# import sqlite3
# connection = sqlite3.connect("students.sqlite3")
# crsr = connection.cursor() 
# crsr.execute('''CREATE TABLE Student (
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(250),
#     age INT,
#     score INT
#     );''')    	
# crsr.execute('''INSERT INTO Student (name,age,score) VALUES('Raj',20,100)''')
# crsr.execute('''INSERT INTO Student (name,age,score) VALUES('Vivek',21,90)''')
# crsr.execute('''INSERT INTO Student (name,age,score) VALUES('Roshan',19,100)''')

class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
    
    @classmethod
    def get(cls,**keys):
        for k,v in keys.items():
            cls.k = k
            cls.v = v
        
        if k not in ('student_id','name','age','score'):
            raise InvalidField
        
        sql_query = "SELECT * FROM student WHERE {} = '{}'".format(cls.k,cls.v)
        k = read_data(sql_query)        
        if(len(k)==0):
            raise DoesNotExist
        elif (len(k)>1):
            raise MultipleObjectsReturned
        else:    
            b=Student(k[0][1],k[0][2],k[0][3])
            b.student_id=k[0][0]
            return b
            
            
    def save(self):
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor()
        if self.student_id == None:
            crsr.execute("INSERT INTO student VALUES (:student_id,:name,:age,:score)",{'student_id':self.student_id,'name':self.name,'age':self.age,'score':self.score}) 
            self.student_id = crsr.lastrowid
        else:
            crsr.execute(f"UPDATE student SET name = \'{self.name}\',age = {self.age},score = {self.score} WHERE student_id = {self.student_id}")
        connection.commit() 
        
    def delete(self):
    	sql_query = ("DELETE FROM student WHERE student_id = {}".format(self.student_id)) 
    	write_data(sql_query)
    
def write_data(sql_query):
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
        crsr.execute(sql_query) 
        connection.commit() 
        connection.close()
     
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
    
        

#student_object = Student(name="Rajini", age=19, score=95)
# student_object.save()
# student_object = Student.get(student_id=1)
# print(student_object.student_id)
# print(student_object.name)
# print(student_object.student_id)

    