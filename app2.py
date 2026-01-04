from flask import Flask
from flask import request, jsonify

app2 = Flask(__name__)

@app2.route('/',methods=['GET'])
def hello():
    return 'Hello World!'

@app2.route('/sum',methods=['GET'])
def sum():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'Введите корректные числа'
    return str(a + b)

if __name__ == '__main__':
    app2.run(debug=True, port=8080)
    