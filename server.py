from flask import Flask
from flask_restful import Resource, Api
from yahoo_finance import Share

app = Flask(__name__)
api = Api(app)

class ShAre(Resource):
    def get(self):
	return "Hi"
	

api.add_resource(ShAre, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
