from flask import Flask, request

app = Flask(__name__)

@app.route("/account/", methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        # Printing the form data
        print(request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        # HTML form for the GET request
        page = '''
        <html>
            <body>
                <form action="/account/" method="POST">
                    <label for="name">Name:</label>
                    <input type="text" name="name" id="name"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body>
        </html>'''
        return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

