from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def echo():
    return '',200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
