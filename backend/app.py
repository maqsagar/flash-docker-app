from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # allow cross-origin requests (for development and docker-compose)


@app.route('/', methods=['GET'])
def health():
return jsonify({'status': 'ok', 'service': 'flask-backend'})


@app.route('/submit', methods=['POST'])
def submit():
# Accept JSON body with keys: name, email, message
try:
data = request.get_json(force=True)
except Exception:
return jsonify({'ok': False, 'error': 'Invalid JSON body'}), 400


name = data.get('name')
email = data.get('email')
message = data.get('message')


# Simple validation
if not name or not email or not message:
return jsonify({'ok': False, 'error': 'name, email and message are required'}), 400


# Process data here (e.g., save to DB, send email...).
# For demo, we'll just return a confirmation with the same data.
result = {
'ok': True,
'received': {
'name': name,
'email': email,
'message': message
},
'note': 'Processed by Flask backend'
}


return jsonify(result), 200


if __name__ == '__main__':
# When running inside Docker in compose, host 0.0.0.0 is required
app.run(host='0.0.0.0', port=5000)