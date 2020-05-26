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
    def filter(cls,**kwargs):
        l = []
        cls.dict = {'gt':'>','lt':'<','gte':'>=','lte':'<=','neq':'<>'}
        for k,v in kwargs.items():
            cls.k = k
            cls.v = v
            p = k.split('__')
            if p[0] not in ('student_id','name','age','score'):
                raise InvalidField
                
            if len(p) == 1:
                sql_query = "{} = '{}'".format(cls.k,cls.v)
            
            elif p[1] == 'in':
                j = tuple(cls.v)
                sql_query = "{} {} {}".format(p[0],p[1],j)
                
            elif p[1] == 'contains':
                sql_query = "{} LIKE '%{}%'".format(p[0],cls.v)
            
            else:
                sql_query = "{} {} '{}'".format(p[0],cls.dict[p[1]],cls.v)
                
            l.append(sql_query)
        k = " and ".join(l)
        k = ' '+k
        #print(k)
        return k
            
              
              
    
            
            
    def save(self):
        import sqlite3
        connection = sqlite3.connect("students.sqlite3")
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
    
    @classmethod    
    def avg(cls,field,**kwargs):
        #print(len(kwargs))
        if field not in ('student_id','name','age','score'):
                raise InvalidField
            
        if len(kwargs) == 0:
            sql_query = ("SELECT AVG({}) FROM Student".format(field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT AVG({}) FROM Student WHERE {}".format(field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
        
    @classmethod    
    def max(cls,field,**kwargs):
        #print(len(kwargs))
        if field not in ('student_id','name','age','score'):
                raise InvalidField
            
        if len(kwargs) == 0:
            sql_query = ("SELECT MAX({}) FROM Student".format(field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT MAX({}) FROM Student WHERE {}".format(field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
            
    @classmethod    
    def min(cls,field,**kwargs):
        #print(len(kwargs))
        if field not in ('student_id','name','age','score'):
                raise InvalidField
            
        if len(kwargs) == 0:
            sql_query = ("SELECT MIN({}) FROM Student".format(field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT MIN({}) FROM Student WHERE {}".format(field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
    
    @classmethod    
    def count(cls,field = None,**kwargs):
        #print(len(kwargs))
        if field == None:
            sql_query = ("SELECT COUNT(*) FROM Student")
        
        elif field not in ('student_id','name','age','score'):
            raise InvalidField
            
        elif len(kwargs) == 0:
            sql_query = ("SELECT COUNT({}) FROM Student".format(field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT COUNT({}) FROM Student WHERE {}".format(field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
            
    @classmethod    
    def sum(cls,field,**kwargs):
        #print(len(kwargs))
        if field not in ('student_id','name','age','score'):
                raise InvalidField
            
        if len(kwargs) == 0:
            sql_query = ("SELECT SUM({}) FROM Student".format(field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT SUM({}) FROM Student WHERE {}".format(field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
    
    
        
    def delete(self):
    	sql_query = ("DELETE FROM Student WHERE student_id = {}".format(self.student_id)) 
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
   
#avg_age = Student.avg('age', age__gt=18, age__lt=21)
#print(avg_age)