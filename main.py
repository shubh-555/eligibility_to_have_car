from flask import Flask,render_template,request
from utils import car_ownership


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data',methods=['POST','GET'])
def get_data():
    data = request.form
    class_object = car_ownership(data)
    result = class_object.car_owner_predict()
    if result == 1:
        return render_template('index.html',prediction ="CONGRATULATIONS ! you are financially healthy ,lets buy a dream car !")
    else:
        return render_template('index.html',prediction = "OOPS ! sorry to say but you can't afford to buy a car right now !")

if __name__=='__main__':
    app.run(host='localhost',port = 5050,debug = True)