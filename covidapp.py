import numpy as np
from flask import Flask,request, jsonify,render_template
import pickle
import pandas as pd
from pandas import DataFrame
########### creating the flask  app
flask_app = Flask(__name__)
model = pickle.load(open("covidmodel.pkl","rb"))

@flask_app.route("/")
def Home():
    return render_template("home.html")
@flask_app.route("/predict",methods =['POST'])
def predict(): # number = [x for x in request.form.values()] which has to be int
    number = [x for x in request.form.values()]
    max1 = pd.to_datetime(number[0], format= "%Y-%m-%d")
    min1 = pd.to_datetime('2021-05-17', format= "%Y-%m-%d")
    delta = max1-min1
    model_prediction= model.forecast(delta.days)
    model_prediction =model_prediction.astype(int)# float  to int conversion 
    a =np.array(model_prediction)
    a=a.tolist()
    result = a

    
    #df = pd.DataFrame(a.values,columns= ["Beds available"])
    return render_template ("home.html",abc= delta.days ,res= result,date_picked =number[0],prediction =result[-1])#prediction_text =a
if __name__ == "__main__":
    flask_app.run(debug=True)







##result = fu.predict(30, model_arima, model_rnn, data, scaler)
        #values = [int(item) for item in result.values]
        #dates = result.index.date
       # res_rnn = fu.forecast_rnn(30,model_rnn,data)
       
    #except:
        #print('some error has occired')
    
    #finally:
        #return render_template('index.html', beds=values,dates=dates,day=len(result),data=True)
