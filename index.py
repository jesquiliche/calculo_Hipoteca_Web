from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
from werkzeug.utils import import_string
from calcular import Calcular_hipoteca
import json

app=Flask(__name__)
app.secret_key="3912481"
# Ruta para acceder al formulario principal, ç
# donde introducimos el capital prestado, el interes anual y el número de años 
# de la hipoteca

@app.route("/")
def Index():
    
    return render_template("index.htm")

@app.route("/calcular",methods=['POST'])  
def Calcular():
    #obtener los valores del forumlario
    capital=int(request.form["Capital"])
    interes=float(request.form["Interes"])
    anos=int(request.form["Anos"])

    # Lllmada a la función que nos devuelve el cuadro 
    # de amortización de la hipoteca.

    cuadro=Calcular_hipoteca(capital,anos,interes)
    flash("Capital : "+str(capital)+"  Interes : "+
    str(interes)+" Años : "+str(anos)+" Hipoteca : ")

    # LLamada al forumulario donde mostramos el cuadro de amortización
    
    return render_template("cuadro.htm",pagos=cuadro)

   



app.run(port=3000,debug=True)

