from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql11518352:tddgw3w2LV@sql11.freemysqlhosting.net/sql11518352'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conn = None

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route("/")
def hello():
    result = Comments.query.all()
    return render_template('index.html', result=result)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api', methods = ['GET', 'POST'])
def homeTest():
    if(request.method == 'GET'):

        data = "Cool! Meine API-Schnittstelle funktioniert! :)"
        return jsonify({'data': data})
