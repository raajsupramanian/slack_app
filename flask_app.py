from flask import Flask
from flask_restful import Resource, Api
from gfin import getQuotes
import json

app = Flask(__name__)
api = Api(app)

class ShAre(Resource):
    def get(self, symbol=None):
	try:
		resp = getQuotes([symbol])
		return resp[0]
	except:
		return "No Data for given code"
api.add_resource(ShAre, '/share/<symbol>', defaults={'symbol': 'ADSK'}, endpoint='GET with symbol')
api.add_resource(ShAre, '/share/', defaults={'symbol': 'ADSK'}, endpoint='GET default')

if __name__ == '__main__':
    app.run(debug=True, port=5002, host="0.0.0.0")
