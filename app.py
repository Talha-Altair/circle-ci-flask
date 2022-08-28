from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def start():

    print("Tutorial")

    return jsonify({"talha":'something'})

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=9000, debug=True)
