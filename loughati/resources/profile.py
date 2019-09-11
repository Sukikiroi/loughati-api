from flask_restful import Resource

class Profile(Resource):
	def get(self):
		return {"method" : "post", "results" : "hello this is an profile", "id" : "p12"}
	def post(self):
		pass
		