import flask
from flask_cors import CORS, cross_origin
from misc import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#get data from the json file
graph,timeHorizon, init_attacker,init_defenders,exits = parseJsonData()
#initialise your environment, defenders etc...
environment=None
defender=None

@app.route("/api/reset", methods=["GET"])
@cross_origin()
def reset():
    global defender
    global environment
    #get data from the json file
    graph,timeHorizon, init_attacker,init_defenders,exits = parseJsonData()
    #initialise your environment, defenders etc...
    environment=None
    defender=None
    #reset your environment/game state etc... below
    return flask.jsonify({'success': True})

#/api/move?node=attacker_new_pos
@app.route("/api/move", methods=["GET"])
@cross_origin()
def move():
    global defender
    global environment
    try:
        #get attacker pos from request params
        attacker_a = int(flask.request.args.get('node'))
        #utilize your env/defender model to retrieve the next defenders position
        defender_a= [] # your next defenders position
        return flask.jsonify({'success': True, 'defenders':[int(i) for i in defender_a]})
    except Exception as e:
        print(e)
        return flask.jsonify({'success': False})

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)