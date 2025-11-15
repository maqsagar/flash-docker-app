# Express (frontend) + Flask (backend) with Docker


## Local (non-Docker) quick run


1. Backend


```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

cd frontend
npm install
npm start
# open http://localhost:3000