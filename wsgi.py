from flask import request, Flask, jsonify
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello, World!"

@app.route('/public-api', methods=['POST'])
@cross_origin(origin='*')
def public_api():
    try:
        data  = json.loads(request.data)
        print('data', data)
        return jsonify(error= False,
                    message= "Success",
                    data=data,
                    statusCode= 200)

    except Exception as err:
        print('public_api err', err)
        return jsonify(error= True,
                    message= "Something went wrong",
                    statusCode=400)