from flask_restful import Resource

class Activity(Resource):
	def get(self):
		return {"method" : "post", "results" : "hello this is an activity", "id" : "a12"}
	def post(self):
		return "hello from Activity"
