class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
    @classmethod
    def get(cls,**keys):
        for k,v in keys.items():
            cls.k = k
            cls.v = v
        
        if k not in ('student_id','name','age','score'):
            raise InvalidField
        
        sql_query = "SELECT * FROM Student WHERE {} = '{}'".format(cls.k,cls.v)
        k = read_data(sql_query)        
        if(len(k)==0):
            raise DoesNotExist
        elif (len(k)>1):
            raise MultipleObjectsReturned
        else:    
            b=Student(k[0][1],k[0][2],k[0][3])
            b.student_id=k[0][0]
            return b
    
    @classmethod
    def filter(cls,**keys):
        
        for k,v in keys.items():
            cls.k = k
            cls.v = v
        
            p = k.split('__')
            if p[0] not in ('student_id','name','age','score'):
                raise InvalidField
                
            if k in ('student_id','name','age','score'):
                l = read_data("SELECT * FROM Student WHERE {} = '{}'".format(cls.k,cls.v))
                    
            elif p[1] == 'gt':
                sql_query = "SELECT * FROM Student WHERE {} > '{}'".format(p[0],cls.v)
                l = read_data(sql_query)   
                            
            elif p[1] == 'lt':
                sql_query = "SELECT * FROM Student WHERE {} <'{}'".format(p[0],cls.v)
                l = read_data(sql_query)   
                            
            elif p[1] == 'gte':
                sql_query = "SELECT * FROM Student WHERE {} >= '{}'".format(p[0],cls.v)
                l = read_data(sql_query) 
                                
            elif p[1] == 'lte':
                sql_query = "SELECT * FROM Student WHERE {} <= '{}'".format(p[0],cls.v)
                l = read_data(sql_query) 
                                
            elif p[1] == 'neq':
                sql_query = "SELECT * FROM Student WHERE {} <> '{}'".format(p[0],cls.v)
                l = read_data(sql_query) 
                            
            elif p[1] == 'in':
                j = tuple(cls.v)
                sql_query = "SELECT * FROM Student WHERE {} in {}".format(p[0],j)
                l = read_data(sql_query) 
                                
            elif p[1] == 'contains':
                sql_query = "SELECT * FROM Student WHERE {} LIKE \'%{}%\'".format(p[0],cls.v)
                l = read_data(sql_query) 
            if len(l) == 0:
                return []
            else:
                out=[]            
                for i in l:
                    b=Student(i[1],i[2],i[3])
                    b.student_id=i[0]
                    out.append(b)
        return out
            
            
    def save(self):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        if self.student_id == None:
            crsr.execute("INSERT INTO Student VALUES (:student_id,:name,:age,:score)",{'student_id':self.student_id,'name':self.name,'age':self.age,'score':self.score}) 
            self.student_id = crsr.lastrowid
            
        elif ("SELECT {} Not in (SELECT student_id FROM student)".format(self.student_id)):
            crsr.execute("INSERT or REPLACE INTO Student VALUES (:student_id,:name,:age,:score)",{'student_id':self.student_id,'name':self.name,'age':self.age,'score':self.score}) 
            self.student_id = crsr.lastrowid
            
        else:
            crsr.execute(f"UPDATE Student SET name = \'{self.name}\',age = {self.age},score = {self.score} WHERE student_id = {self.student_id}")
        connection.commit() 
        
    def delete(self):
    	sql_query = ("DELETE FROM Student WHERE student_id = {}".format(self.student_id)) 
    	write_data(sql_query)
    
def write_data(sql_query):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
        crsr.execute(sql_query) 
        connection.commit() 
        connection.close()
     
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans
    
        
# selected_students = Student.filter(name = "jessie")

# selected_students = Student.filter(age__in=[25,34],score__lt=50)
# print(selected_students)