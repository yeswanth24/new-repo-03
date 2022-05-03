from config import db

class DbPerson(db.Model):
    __tablename__='emp'
    eno=db.Column(db.String(30),primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    desig=db.Column(db.String(30),index=False,unique=False,nullable=False)
    age=db.Column(db.Integer(30),index=False,unique=False,nullable=False)
    

    def __init__(self,eno,name,city,desig,age):
        self.eno=eno
        self.name=name
        self.city=city
        self.desig=desig
        self.age=age
    
    def serialize(self):
        return {
            'eno':self.eno,
            'name':self.name,
            'city':self.city,
            'desig':self.desig,
            'age':self.age
            }
    
    def __repr__(self):
        return str(self.serialize())