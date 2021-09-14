from flask import request, Flask
import json

app3 = Flask(__name__)
@app3.route('/')
def hello_world():
    return 'Hello, Diego te saludo desde el Flask de la app3'
if __name__ == '__main__':
    app3.run(debug=True, host='0.0.0.0')