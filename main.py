from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/health',methods=['GET'])
def healthCheck():
    ok={'health':'ok'}
    resp=make_response(ok)
    return resp


@app.route('/',methods=['GET','POST'])
def hello_world():
    print(request)
    print(request.data)
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
