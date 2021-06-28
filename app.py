from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route('/')
def start():

    # print("soemthing")

    return jsonify({"talha":'something'})

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=9000, debug=True)

  # app_1 = app.test_client()

  # response =  app_1.get('/')

  # print(response.get_data())
