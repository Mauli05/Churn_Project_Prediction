# from re import X
from flask import Flask,render_template,request,url_for
import pickle
import numpy as np
import pandas as pd


# create an object of the class "Flask" by passing first argument.
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__,template_folder='Template')
# app = Flask(__name__,static_folder='Statics')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods = ["POST"])
def predict():
   
    accountlength=float(request.form.get("accountlength",False))
    internationalplan=float(request.form.get("internationalplan",False))
    voicemailplan=float(request.form.get("voicemailplan",False))
    numbervmailmessages=float(request.form.get("numbervmailmessages",False))
    totaldayminutes=float(request.form.get("totaldayminutes",False))
    totaldaycalls=float(request.form.get("totaldaycalls",False))
    totaldaycharge=float(request.form.get("totaldaycharge",False))
    totaleveminutes=float(request.form.get("totaleveminutes",False))
    totalevecalls=float(request.form.get("totalevecalls",False))
    totalevecharge=float(request.form.get("totalevecharge",False))
    totalnightminutes=float(request.form.get("totalnightminutes",False))
    totalnightcalls=float(request.form.get("totalnightcalls",False))
    totalnightcharge=float(request.form.get("totalnightcharge",False))
    totalintlminutes=float(request.form.get("totalintlminutes",False))
    totalintlcalls=float(request.form.get("totalintlcalls",False))
    totalintlcharge=float(request.form.get("totalintlcharge",False))
    numbercustomerservicecalls=float(request.form.get("numbercustomerservicecalls",False))   


    output = model.predict(np.array([accountlength, internationalplan, voicemailplan,
       numbervmailmessages, totaldayminutes, totaldaycalls,
       totaldaycharge, totaleveminutes, totalevecalls, totalevecharge,
       totalnightminutes, totalnightcalls, totalnightcharge,
       totalintlminutes, totalintlcalls, totalintlcharge,
       numbercustomerservicecalls]).reshape(1,17))
            

    if output==1:
        return "<h1 style='color:red'> Customer has Churn</h1>"
    else:
        return "<h1 style='color:green'> Customer not Churn </h1>"
   

# if __name__=="__main__": 
#     app.run(debug=True)
