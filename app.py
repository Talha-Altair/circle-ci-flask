from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():

    print("soemthing")

    return render_template('index.html',value="9000 wala port")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9000, debug=True)
