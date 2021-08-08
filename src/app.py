from flask import Flask
from flask_restx import Resource, Api, reqparse
from geneticAlgo.solve import start

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('numColors', type=int, help='numer of colors in the pool')
parser.add_argument('target', type=int, action='split', help='target')

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

@api.route('/genetic-algo')
class Ga(Resource):
  @api.expect(parser)
  def post(self):
    args = parser.parse_args()
    print(args['target'])
    return {'hello': 'world'}

if __name__ == '__main__':
  app.run(debug=True)