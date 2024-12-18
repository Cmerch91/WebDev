from flask import Flask, request

app = Flask(__name__)

@app.route("/hello/")
def hello():
    # Correct the typo here (from 'arge' to 'args')
    name = request.args.get('name', '')  

    if name == '':
        return "No param supplied"
    else:
        return "Hello %s" % name

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
