from flask import request,jsonify
from flask_restful import Resource
from .model import db , User
import re
def valide_user_data(data):
    mailreg = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if data["userName"] is None :
        return False,"user name is missing"
    if data["password"] is None :
        return False,"password is missing"
    if data["FName"] is None :
        return False ,"first name is missing"
    elif not  re.sub("\s","",str(data["FName"])).isalpha():
        return  False , "first name contains only alphabetical characters"
    if data["LName"] is None :
        return False ,"last name is missing"
    elif not re.sub("\s","",str(data["FName"])).isalpha():
        return  False , "last name contains only alphabetical characters"
    if data["Email"] is None :
        return False , "email is missing"
    if not re.fullmatch(mailreg,data["Email"]):
        return False ,"invalid email"
    return True,"user {} created ! ".format(data["userName"])

class Register(Resource):
    def post(self):
        data = request.get_json()
        if data : 
            validator = valide_user_data(data)
            if  validator[0]: 
                db.session.add(User(data["userName"],data["password"],data["FName"],data["LName"],data["Email"]))
                db.session.commit()
                return jsonify({"result":"success","description" :validator[1]})
            else :
                return jsonify({"result":"error","description" :validator[1]})
        else:
            data = request.form
            if data : 
                validator = valide_user_data(data)
                if  validator[0]: 
                    db.session.add(User(data["userName"],data["password"],data["FName"],data["LName"],data["Email"]))
                    db.session.commit()
                    return jsonify({"result":"success","description" :validator[1]})
                else:
                    return jsonify({"result":"error","description" :validator[1]})

