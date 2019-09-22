from flask import request,jsonify,session
from flask_restful import Resource
from flask_bcrypt import Bcrypt




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
        if 'user' in session:
            return jsonify({"data":"{} Logged in".format(session['user'])})
        data = request.get_json()
        if not data : data = request.form
        if data : 
            validator = valide_user_data(data)
            if  validator[0]: 
                db.session.add(User(data["userName"],data["password"],data["FName"],data["LName"],data["Email"]))
                db.session.commit()
                return jsonify({"result":"success","description" :validator[1]})
            else :
                return jsonify({"result":"error","description" :validator[1]})
        else :
            return jsonify({"status":"data not found"})
       
class Login(Resource):
    def post(self):
        print(request.headers)
        data = request.get_json()
        print(data) 
        if not data : data = request.form 
        print(data)  
        user = User.query.filter_by(userName=data["userName"]).first()
        if user and data["password"] == user.password :
            session['user'] = user.userName
            return jsonify({"result":"succes","decription":'{} logged in !'.format(data['userName'])})
        return jsonify({"satuts":"tnawet"})

class Logout(Resource):
    def post(self):
        print("aha hawchouni")
        session.pop('user') 
        return "disconnected"
class Status(Resource):
    def post(self):
        
        if 'user' in session:
            return jsonify({"status":True})
        return jsonify({"status":False})