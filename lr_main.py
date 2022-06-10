# importing the lib
from flask import Flask , render_template, request
import joblib

app = Flask(__name__)

#load the model
model = joblib.load('model/sales.pkl')

@app.route('/')
def home():
    return render_template('lr_home.html')

@app.route('/data', methods=['post'])
def data():
    TV = request.form.get('TV')
    Radio = request.form.get('Radio')
    Newspaper = request.form.get('Newspaper')
    

    result = model.predict([[TV,Radio,Newspaper]])

    data = result
  
    return render_template('lr_predict.html',data=data)

app.run(host = '0.0.0.0', port = 8080) # should be always at the end


"""
http: hyper text transfer protocol
127.0.0.1 - ip address - localhost
:5000 - port
/ - route

http://127.0.0.1:5000/

"""