import os
import json
from flask import Flask, request

app = Flask(__name__)
registration_file = None

@app.route('/')
def adminHome():
    return 'Welcome to admin Page!!!'

@app.route('/users')
def getAllUsers():
    users = getUserDetails()
    if len(users) <= 0:
        return "No user registered yet!!!"
    else:
        return {'Available Users': [user['uname'] for user in users]}

@app.route('/user/<uname>')
def getUserData(uname):
    users = getUserDetails()
    print('uname:',uname)
    for user in users:
        print(user)
        if user['uname'] == uname:
            return user
    return "{} not found!!!".format(uname)


def getUserDetails():
    feeds = []
    if not os.path.isfile(registration_file):
        return feeds

    with open(registration_file) as feedsjson:
        feeds = json.load(feedsjson)

    return feeds

if __name__ == '__main__':
    registration_file = os.environ['REG_FILE']
    app.run(host=os.environ['FLASKHOSTNAME'],
            port=os.environ['FLASKPORT'],
            debug=True)
