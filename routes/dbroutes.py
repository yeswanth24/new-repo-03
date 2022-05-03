from config import app,db
from flask import jsonify,request,abort
from models import DbPerson

@app.route("/emp")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)


@app.route("/emp",methods=['POST'])
def processDepartments():
    try:
        input=request.get_json()
        eno=input['eno']
        name=input['name']
        city=input['city']
        desig=input['desig']
        age=input['age']
        db.session.add(DbPerson(eno,name,city,desig,age))
        db.session.commit()
        return {"status": "success"}, 201
    except:
        abort({'status':"Internal server error"},500)