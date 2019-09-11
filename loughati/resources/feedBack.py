from flask_restful import Resource

class FeedBack(Resource):
	def get(self):
		return {"method" : "post", "results" : "hello this is an feedback", "id" : "f12"}
	def post(self):
		pass
		