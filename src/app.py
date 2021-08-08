from flask import Flask, request
from flask_cors import CORS, cross_origin
from geneticAlgo.solve import start

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route("/")
@cross_origin()
def hello_world():
  return "<p>Hello, World!</p>"

@app.route('/genetic-algo', methods=['POST'])
@cross_origin()
def json_example():
  request_data = request.get_json()
  numColors, target = request_data['numColors'], request_data['target']
  print(numColors)
  print(target)
  answer_num = [COLORS_INDEX.get(color) for color in target]
  board, state = start(answer_num, False, numColors)
  print(board)
  return {'board': board, 'state': state }

if __name__ == '__main__':
  app.run(debug=True)