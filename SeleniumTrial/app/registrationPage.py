import os
from flask import Flask, render_template, request
app = Flask(__name__)

path = "../data/"

# Gets file names without the file extension
CLASSNAMES = [os.path.splitext(filename)[0] for filename in os.listdir(path)]


@app.route("/")
def template_test():
    return render_template('index.html', classNames = CLASSNAMES)

@app.route("/info", methods=['POST'])
def getinfo():
    test = request.form.getlist('boxes')
    final = ""
    for i in range(len(test)):
        final += str(test[i])
    return final

if __name__ == '__main__':
    app.run(debug=True)
