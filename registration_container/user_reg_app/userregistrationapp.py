import os
import json
from flask import Flask, request

app = Flask(__name__)
registration_file = None

@app.route('/')
def userHome():
    return 'Hello World!'

@app.route('/signup', methods = ['GET', 'POST'])
def userSignup():

    if request.method == 'GET':
        return {"Message": "Welcome to Flask User Registration!!!",
                "Registration": "Signup with username, mail, firstname and lastname",
                }
    else:
        user_details = dict()
        user_details['uname'] = request.form.get('username', '')
        user_details['pwd'] = request.form.get('pwd','')
        user_details['fname'] = request.form.get('fname','')
        user_details['lname'] = request.form.get('lname','')
        registerUser(user_details)
        return {'welcome':user_details['fname'] + ' ' + user_details['lname'],
                'registration': 'Successfully Registered !!!'}

def registerUser(user_details):
    feeds = []
    if os.path.isfile(registration_file):
        with open(registration_file) as feedsjson:
            feeds = json.load(feedsjson)

    feeds.append(user_details)
    with open(registration_file, 'w') as fp:
        fp.write(json.dumps(feeds, indent=2))

if __name__ == "__main__":
    print(os.environ['CODER'])
    registration_file = os.environ['REG_FILE']
    app.run(host=os.environ['FLASKHOSTNAME'],
            port=os.environ['FLASKPORT'],
            debug=True)

