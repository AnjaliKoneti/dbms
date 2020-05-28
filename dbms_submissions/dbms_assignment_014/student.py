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
            
              
    @classmethod    
    def aggregate(cls,method,field,**kwargs):
        #print(len(kwargs))
        if field not in ('student_id','name','age','score'):
                raise InvalidField
            
        if len(kwargs) == 0:
            sql_query = ("SELECT {}({}) FROM Student".format(method,field))
        else:
            print(kwargs)
            j = Student.filter(**kwargs)
            sql_query = ("SELECT {}({}) FROM Student WHERE {}".format(method,field,j))
        r = read_data(sql_query)
        #print(r)
        for i in r:
            return i[0]
        
    @classmethod    
    def max(cls,field,**kwargs):
        #print(len(kwargs))
        k = Student.aggregate("max",field,**kwargs)
        return k
    
    @classmethod    
    def avg(cls,field,**kwargs):
        #print(len(kwargs))
        k = Student.aggregate("AVG",field,**kwargs)
        return k
    
            
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