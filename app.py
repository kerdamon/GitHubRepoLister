from flask import Flask
from flask_cors import CORS
from controllers import rep

app = Flask(__name__)
CORS(app)

app.register_blueprint(rep)

if __name__ == '__main__':
    app.run()