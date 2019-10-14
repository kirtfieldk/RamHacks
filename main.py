# For RamHAcks 2019 the challenge is 
# Capital One FInance Hack 
# Flask as backend and JS as front end
# User types in their credit score and we recomend good credit cards



from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/api/creditcards',  methods=['GET'])
def allCreditCards():
    # TODO DIsplay all credit cards
    return



@app.route('/api/addcreditcard',  methods=['POST'])
def addCreditCard(id):
    #TODO Add a credit card
    request.headers['Content-Type'] == 'application/json'
    return "JSON Message: " + json.dumps(request.json)


@app.route('/api/creditcard/<creditscore>', methods=['GET'])
def matchCardToScore(creditScore):
    #TODO matches credit card with credit score
    return

@app.route('/api/adduser/<user>', methods=['POST'])
def addUser(user):
    #TODO add a user when they sign up
    
    # request.headers['Content-Type'] == 'application/json'
    return request.json

@app.route('/api/getuser/<task_id>', methods=['GET'])
def getUser(task_id):
    #TODO add a user when they sign up
    request.headers['Content-Type'] == 'application/json'
    return "JSON Message: " + json.dumps(request.json)

@app.route('/api/updateUser', methods=['PUT'])
def updateUser(user):
    #TODO update a users info
    request.headers['Content-Type'] == 'application/json'
    return "JSON Message: " + json.dumps(request.json)



def calcPayoffPeriod(timeFrame, cost):
    return cost / timeFram






if __name__ == '__main__':
    app.run()