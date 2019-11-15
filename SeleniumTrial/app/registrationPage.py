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
    # Classes user has signed up for
    classes = request.form.getlist('boxes')

    # Contains name and email
    user_info = request.form.getlist('user-info')
    final = ""
    classes.extend(user_info)

    for i in range(len(classes)):
        final += str(classes[i])
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
