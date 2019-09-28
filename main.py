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
@app.route('/api/addcreditcard', id,  methods=['POST'])
def addCreditCard(id):
    #TODO Add a credit card
@app.route('/api/creditcard/creditscore', creditScore, metods=['GET'])
def matchCardToScore(creditScore):
    #TODO matches credit card with credit score
@app.route('/api/adduser', user, methods=['POST'])
def addUser(user):
    #TODO add a user when they sign up
@app.route('/api/getuser/<int:task_id>', user, methods=['GET'])
def getUser(task_id):
    #TODO add a user when they sign up


if __name__ == '__main__':
    app.run()