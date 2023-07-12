from flask import Flask
from dotenv import load_dotenv
from handlers.http_handler import app

load_dotenv()
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)