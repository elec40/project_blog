from pymongo import MongoClient

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.proj_blog

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/sign_up')
def sign_up():
   return render_template('sign_up.html')


@app.route('/search_id', methods=['GET'])
def test_get():
   user_id = db.login.find_one({'id':'bobby'})
   return jsonify({'msg': user_id})

@app.route('/create_id', methods=['POST'])
def delete_star():
   receive_user_id = request.form['user_id']
   return jsonify({'msg': receive_user_id})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)