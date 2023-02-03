from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
from werkzeug.utils import import_string
from calcular import Calcular_hipoteca
import json

app=Flask(__name__)
app.secret_key="3912481"
@app.route("/")
def Index():
    
    return render_template("index.htm")

@app.route("/calcular",methods=['POST'])  
def Calcular():
    capital=int(request.form["Capital"])
    interes=float(request.form["Interes"])
    anos=int(request.form["Anos"])
    print(capital)
    print(interes)
    print("anos")
    cuadro=Calcular_hipoteca(capital,anos,interes)
    flash("Capital : "+str(capital)+"  Interes : "+
    str(interes)+" Años : "+str(anos)+" Hipoteca : ")
    
    return render_template("cuadro.htm",pagos=cuadro)

   



app.run(port=3000,debug=True)

