from flask import Flask
from flask import request
from flask_restful import Resource, Api
from gfin import getQuotes
import json

app = Flask(__name__)
api = Api(app)

class ShAre(Resource):
    def get(self):
	symbol = request.args.get('text')
	if not symbol:
		symbol = "ADSK"
	try:
		resp = getQuotes([symbol])
		return resp[0]
	except:
		return "No Data for given code"
api.add_resource(ShAre, '/share', endpoint='GET default')

if __name__ == '__main__':
    app.run(debug=True, port=5002, host="0.0.0.0")
