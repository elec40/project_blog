from pymongo import MongoClient

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.proj_blog

@app.route('/')
def home_page():
   return render_template('index.html')

@app.route('/login')
def login_page():
   return render_template('login.html')

@app.route('/sign_up')
def sign_up_page():
   return render_template('sign_up.html')

@app.route('/main')
def main_page():
   return render_template('main.html')


@app.route('/sign_up/check_id', methods=['POST'])
def check_id():
   receive_user_id = request.form['user_id']

   user_id = db.login.find_one({'user_id': receive_user_id})

   if user_id == None:
      return jsonify({'result': 1})
   else:
      return jsonify({'result': 2})

@app.route('/sign_up/create_id', methods=['POST'])
def create_id():
   receive_user_id = request.form['user_id']
   receive_user_password = request.form['user_password']

   db.login.insert_one({'user_id': receive_user_id, 'user_password': receive_user_password})

   return jsonify({'msg': "생성 완료\n로그인 페이지로 이동합니다."})

@app.route('/login', methods=['POST'])
def login():
   receive_user_id = request.form['user_id']
   receive_user_password = request.form['user_password']

   user_id = db.login.find_one({'user_id': receive_user_id}, {'user_password': receive_user_password})

   print(user_id)

   if user_id == None:
      return jsonify({'result': 1})
   else:
      return jsonify({'result': 2})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)