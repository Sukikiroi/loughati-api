from flask import Flask
from flask_restful import Api, Resource
from loughati.resources.dico import Dico
from loughati.resources.feedBack import FeedBack
from loughati.resources.profile import Profile
from loughati.resources.activity import Activity
from loughati.resources.register import Register
from loughati import app

api = Api(app)

api.add_resource(Dico, '/dico')
api.add_resource(FeedBack, '/feedback')
api.add_resource(Profile, '/profile')
api.add_resource(Activity, '/activity')
api.add_resource(Register,'/register')

if __name__ == '__main__':
    app.run(debug=True)

