from flask import Flask ,escape,request,render_template
import pickle
import numpy as np
app=Flask(__name__)
reg=pickle.load(open('xgboost_regressor.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Tmax = int(request.form['TM'])
        Tmin = int(request.form['Tm'])
        T = int(request.form['T'])
        H = int(request.form['H'])
        SLP = int(request.form['SLP'])
        # rain = float(request.form['rain'])
        VV = float(request.form['VV'])
        V = float(request.form['V'])
        VM = float(request.form['VM'])
        # age = int(request.form['age'])


        data=np.array([[T,Tmax,Tmin,SLP,H,VV,V,VM]])
        prediction=reg.predict(data)
        if 0<prediction<50:
            ran="Your City has Good AQI Value"
            col='#00df00'
        elif 51<prediction<100:
            ran="Your City has Moderate AQI Value"
            col='#ffff00'
        elif 101<prediction<150:
            ran="Your City has Unhealthy For Sensitive Group AQI Value"
            col="#ff6b00"
        elif 151<prediction<200:
            ran="Your City has  Unhealthy AQI Value"   
            col="#ff0000" 
        elif 200<prediction<300:
            ran="Your City has Very Unhealthy AQI Value"
            col="#880039"
        else:
            ran="Your City has Very Hazardous AQI Value"
            col='#6b0016'






        return render_template ("prediction.html",prediction_text=(round(prediction[0],4)),about=ran,color=col)

    else:
        return render_template("prediction.html")








if __name__=="__main__":
    app.run(debug=True)                   
