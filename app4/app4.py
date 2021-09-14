from flask import request, Flask
import json

app4 = Flask(__name__)
@app4.route('/')
def hello_world():
    return 'Hello, Diego te saludo desde el Flask de la app4'
if __name__ == '__main__':
    app4.run(debug=True, host='0.0.0.0')