from flask import request, Flask
import json

app2 = Flask(__name__)
@app2.route('/')
def hello_world():
    return 'Hello, Diego te saludo desde el Flask de la app2'
if __name__ == '__main__':
    app2.run(debug=True, host='0.0.0.0')