# AQI-Prediction
# Air-Quality-Index-Prediction-Forecast
# Why is air quality important? 

Local air quality affects how you live and breathe. Like the weather, it can change from day to day or even hour to hour. 
The U.S. Environmental Protection Agency (EPA) and your local air quality agency have been working to make information about outdoor air quality as easy to find and understand as weather forecasts. 
A key tool in this effort is the Air Quality Index, or AQI. EPA and local officials use the AQI to provide simple information about your local air quality, how unhealthy air may affect you, and how you can protect your health.




# What is the AQI?
The AQI is an index for reporting daily air quality. It tells you how clean or unhealthy your air is, and what associated health effects might be a concern. The AQI focuses on health affects you may experience within a few hours or days after breathing unhealthy air. 
In this Machine Learning Model Our main ain is to predict the AQI value of the area by knowing some information about the environment like temperature, visibility, wind speed, rainfall, pressure, etc

# Data Description 
 
We will be using Air Quality Index AQI Data Set from Krish naik YouTube in GitHub Machine Learning Repository. This Data set is satisfying our data requirement
 
# Export Data from CSV for Training 
 
Here we will be exporting all batches of data f into one csv file for training. 
 
# Data Splitting 
 
We split the data here for our train and test data for further uses.


# Data Pre-processing 
 
We will be exploring our data set here and perform data pre-processing depending on the data set. 
We first explore our data set in Jupyter Notebook and decide what pre-processing and validation we have convert categorical values to numerical values by encoding and then we have to write separate modules according to our analysis, so that we can implement that for training as well as prediction data. Also we have to convert date into proper date time format for future forecasting 
 	 
 # Model Training 
 
We trained various model in our notebook and XGBoost Regressor was good on it. We trained with our processed data. 
 
 
# Model Evaluation 
 
Model evaluation done by Root Mean Square Error (RMSE) which was quite low about 13.8594

 
# Model Saving 
 
We will save our models so that we can use them for prediction purpose.  
 
# Push to app** 
 	 
Here we will do cloud setup for model deployment. We also create our Flask app and user interface and integrate our model with Flask app and UI. 
 
 
# Data from client side for prediction and Forecast purpose

Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side.  


# Displaying Prediction in Line Graph

Finally, After the model has successfully forecasted the AQI then our webpage will plot the graph of forecasted value for user interaction

# Deployed at:https://aqiprediction03.herokuapp.com/
# Linkedin :https://www.linkedin.com/posts/deepak-prasad-33b35b22b_ai-ineuron-deeplearning-activity-6906886614849830912-kwGL

# Video Demo: https://drive.google.com/file/d/1EjpZZQtiD1AvQmVhkIddZ3ZBqfwBljg0/view?usp=sharing
