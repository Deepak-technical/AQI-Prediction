from flask import Flask ,escape,request,render_template
import pickle
import plotly.express as px
import plotly
import json
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


@app.route('/forecast',methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        city=request.form["city"]
        import pandas as pd
        df=pd.read_csv('./data/city_day.csv')
        
        df['Date']=pd.to_datetime(df['Date'])
        Mumbai = df[df['City'] == city]
        from fbprophet import Prophet 

        Mumbai_data = Mumbai[['Date','AQI']]
        Mumbai_data.reset_index(inplace = True,drop = True)

        #Defining our training dataset
        train_df = Mumbai_data
        train_df.rename(mapper = {'Date':'ds','AQI':'y'},axis =1,inplace = True)
        model = Prophet(holidays_prior_scale=0,seasonality_prior_scale=365,n_changepoints= 50,)
        model.fit(train_df)
        future = model.make_future_dataframe(periods=365)
        future.tail()
        #Forecasting the AQI values
        forecast = model.predict(future)
        forecast.tail()
        predected=forecast.iloc[2000:,:]
        newDate=predected['ds'].to_numpy()
        newData=predected['yhat'].to_numpy()
        davg=(np.average(newData))
        # newData.plot(x='ds',y='yhat')
        df2 = pd.DataFrame({
                "Years(2020-2021)": newDate,
                "Predicted AQI(Air Quality Index)": newData
                

            }) 

        fig = px.line(df2, x="Years(2020-2021)",
                        y="Predicted AQI(Air Quality Index)",title=f'Predicted AQI of  in 2020-2021')
        fig.update_traces(line_color='green')    
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('forecast.html', graphJSON=graphJSON,paqi=round(davg,4),city=city )

    else:
        return render_template('forecast.html')    





if __name__=="__main__":
    app.run(debug=True)                   