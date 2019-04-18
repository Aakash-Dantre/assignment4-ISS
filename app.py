from flask import Flask
from flask import render_template
from flask import session
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
# from functools import wraps
from flask import request
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    root = db.Column(db.String(80), unique=False)
    addsingdr = db.Column(db.String(80), unique=False)
    addpludr = db.Column(db.String(80), unique=False)
    addsingob = db.Column(db.String(80), unique=False)
    addpluob = db.Column(db.String(80), unique=False)
    delsingdr = db.Column(db.String(80), unique=False)
    delpludr = db.Column(db.String(80), unique=False)
    delsingob = db.Column(db.String(80), unique=False)
    delpluob = db.Column(db.String(80), unique=False)

    def __init__(self, root, addsingdr, addpludr, addsingob, addpluob, delsingdr, delpludr, delsingob, delpluob):
        self.root = root
        self.addpludr = addpludr
        self.addsingob = addsingob
        self.addpluob = addpluob
        self.delsingdr = delsingdr
        self.delpludr = delpludr
        self.delsingob = delsingob
        self.delpluob = delpluob

# app.run(host='http://0.0.0.0', port=5000, debug=False)

@app.errorhandler(404)
def not_found(error):
	return "Nothing found<br>Try something else.<br>"
	# return render_template('Introduction.html'), 200

@app.route("/")
@app.route("/home", methods=["GET"])
def home():
	return render_template('Introduction.html')

@app.route("/experiment", methods=["GET"])
@app.route("/Experiment.html", methods=["GET"])
def experiment():
    result=[-1,-1,-1,-1]
    return render_template('Experiment.html',result=result,flag=0,var=0,root=0)


@app.route("/feedback", methods=["GET"])
def feedback():
	return render_template('Feedback.html')

@app.route("/readings", methods=["GET"])
def readings():
	return render_template('Further Readings.html')

@app.route("/objective", methods=["GET"])
def objective():
	return render_template('Objective.html')

@app.route("/procedure", methods=["GET"])
def procedure():
	return render_template('Procedure.html')

@app.route("/quizzes", methods=["GET"])
def quizzes():
	return render_template('Quizzes.html')

@app.route("/theory", methods=["GET"])
def theory():
	return render_template('Theory.html')

@app.route("/<page>", methods=["GET"])
def loadpath(page):
	return render_template(page)

@app.route("/Experiment.html", methods=["POST"])
def userAdd():
    root=request.form['root']
    addsingdr=request.form['addsingdr']
    addpludr=request.form['addpludr']
    addsingob=request.form['addsingob']
    addpluob=request.form['addpluob']
    delsingdr=request.form['delsingdr']
    delpludr=request.form['delpludr']
    delsingob=request.form['delsingob']
    delpluob=request.form['delpluob']
    db.create_all()
    new_entry=User(root, addsingdr, addpludr, addsingob, addpluob, delsingdr, delpludr, delsingob, delpluob)
    db.session.add(new_entry)
    db.session.commit()
    temp ={}
    temp['status']=(type(new_entry)==User)
    # ans[4][8]=[6571537,3946843,857157,3882417]
    ans =[[0,0,0,0,0,6,6,7],[5,5,5,5,5,3,5,4],[0,0,0,0,0,2,0,1],[5,5,5,5,5,5,5,4]]
    inpt=[delsingdr,delpludr,delsingob,delpluob,addsingdr,addpludr,addsingob,addpluob]
    corr_ans=ans[int(root)]
    count =0
    result=[0,0,0,0]
    for i in range(8):
        if corr_ans[i]==int(inpt[i]):
            count+=1
            result[i%4]+=1
        
    var=0
    if count==8 :
        var=1
    return render_template('Experiment.html',result=result,flag=1,var=var,root=root)

if __name__ == "__main__":
	# app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)


