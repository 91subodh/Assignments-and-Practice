from flask import Flask, render_template, request
import loadfunction

app = Flask(__name__)

@app.route('/front')
def upload_file():
    return render_template('GetContext.html')


@app.route('/rc', methods=['GET', 'POST'])
def return_context():
    if request.method == 'POST':
        f = request.files['file']
        l = loadfunction.return_context('/Users/home/Desktop/' + f.filename)
        return str(l)


if __name__ == '__main__':
    app.run(debug=True)
