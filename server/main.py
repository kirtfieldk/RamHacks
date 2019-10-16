# For RamHAcks 2019 the challenge is 
# Capital One FInance Hack 
# Flask as backend and JS as front end
# User types in their credit score and we recomend good credit cards

from flask import Flask, jsonify, make_response, request
import sqlite3

# COnnect and create databse
app = Flask(__name__)
def defincrsr():
    connection = sqlite3.connect("creditcard.db")
    crsr = connection.cursor()
    return crsr
@app.route('/')
def hello_world():
    crsr = defincrsr()
    cards = []
    crsr.execute("SELECT * FROM creditcards") 
    result = crsr.fetchall() 
    for r in result:
        cards.append(r)
    return jsonify(cards)
@app.route('/api/creditcards',  methods=['GET'])
def allCreditCards():
    # TODO DIsplay all credit cards
    return



@app.route('/api/addcreditcard',  methods=['POST'])
def addCreditCard(id):
    #TODO Add a credit card
    request.headers['Content-Type'] == 'application/json'
    return "JSON Message: " + json.dumps(request.json)


@app.route('/api/creditcard/<int:creditscore>', methods=['GET'])
def matchCardToScore(creditscore):
    crsr = defincrsr()
    cmd = """SELECT name FROM creditcards WHERE credit_low <= '{cs}' AND '{cs}' <= credit_high""".format(cs=creditscore)
    crsr.execute(cmd)
    result = crsr.fetchall()    
    return jsonify(result)

@app.route('/api/adduser/<user>', methods=['POST'])
def addUser(user):
    #TODO add a user when they sign up
    
    # request.headers['Content-Type'] == 'application/json'
    return request.json

@app.route('/api/getuser/<int:id>', methods=['GET'])
def getUser(id):
    #TODO add a user when they sign up
    crsr = defincrsr()
    cmd = """SELECT name FROM creditcards WHERE id='{id}'""".format(id=id)
    crsr.execute(cmd)
    result = crsr.fetchall()
    return jsonify(result)
    

@app.route('/api/updateUser/<int:user>', methods=['PUT'])
def updateUser(user):
    #TODO update a users info
    if len(user) == 0:
        abort(404)
    cmd = """"""
    
    request.headers['Content-Type'] == 'application/json'
    return "JSON Message: " + json.dumps(request.json)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def calcPayoffPeriod(timeFrame, cost):
    return cost / timeFram






if __name__ == '__main__':
    app.run(debug=True)