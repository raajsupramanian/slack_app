from flask import Flask
from flask_restful import Resource, Api
from yahoo_finance import Share

app = Flask(__name__)
api = Api(app)

class ShAre(Resource):
    def get(self, shareid):
	ad = Share(shareid)
	return {'open_price': ad.get_open(), 'price': ad.get_price(), 'change':ad.get_change()}
	

api.add_resource(ShAre, '/<string:shareid>')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
