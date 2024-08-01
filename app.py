#this is only for deployment purpose as this will deploy on sever so it can run continously 24/7 . 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bnsl_boy'


if __name__ == "__main__":
    app.run()
