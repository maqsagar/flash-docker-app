from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os


app = Flask(__name__)
CORS(app)


# MongoDB connection (use environment variable MONGO_URI)
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/')
client = MongoClient(mongo_uri)
db = client['formdb']
collection = db['submissions']


@app.route('/', methods=['GET'])
def health():
return jsonify({'status': 'ok', 'service': 'flask-backend', 'db': 'connected'})


@app.route('/submit', methods=['POST'])
def submit():
data = request.get_json(force=True)


name = data.get('name')
email = data.get('email')
message = data.get('message')


if not all([name, email, message]):
return jsonify({'ok': False, 'error': 'Missing fields'}), 400


doc_id = collection.insert_one({
'name': name,
'email': email,
'message': message
}).inserted_id


return jsonify({'ok': True, 'inserted_id': str(doc_id)})


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)