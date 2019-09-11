from flask_restful import Resource

class Dico(Resource):
	def get(self):
		return {"method" : "post", "results" : "hello this is an dico", "id" : "d12"}
	def post(self):
		return "hello from dico"
		