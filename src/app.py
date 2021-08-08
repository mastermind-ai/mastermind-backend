from flask import Flask
from flask_restx import Resource, Api, reqparse
from geneticAlgo.solve import start

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('numColors', type=int, help='numer of colors in the pool')
parser.add_argument('target', type=str, action='split', help='target')

INDEX_COLORS = {
  0: "red",
  1: "blue",
  2: "green",
  3: "purple",
  4: "yellow",
  5: "orange",
}

COLORS_INDEX = {
  "red": 0,
  "blue": 1 ,
  "green": 2,
  "purple": 3,
  "yellow": 4,
  "orange": 5,
}

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

@api.route('/genetic-algo')
class Ga(Resource):
  @api.expect(parser)
  def post(self):
    args = parser.parse_args()
    numColors, target = args['numColors'], args['target']
    answer_num = [COLORS_INDEX.get(color) for color in target]
    board, state = start(answer_num, False, numColors)
    return {'board': board, 'state': state}

if __name__ == '__main__':
  app.run(debug=True)