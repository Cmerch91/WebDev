from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/account/", methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/file.png')
        return "<img src='" + url_for('static', filename='uploads/file.png') + "'/>"
    else:
        page = '''
        <html>
            <body>
                <form action="" method="post" enctype="multipart/form-data">
                    <input type="file" name="datafile"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body>
        </html>
        '''
        return page, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

