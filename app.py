from flask import Flask, render_template

app = Flask(__name__)

data = dict()
reviews = ['Good product', 'Bad product', 'I like it']
positive = 1
negetive = 0

@app.route("/")

def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negetive'] = negetive

    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run()