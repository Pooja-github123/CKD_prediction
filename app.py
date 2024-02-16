from flask import Flask,request,render_template
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('CKDmodel.pkl','rb'))
@app.route('/')
def page():
    return render_template('index.html')

@app.route('/predict',methods=["GET" , "POST"])
def predict():
    try:
       data1= int(request.form['a'])
       data2= float(request.form['b'])
       data3= float(request.form['c'])
       data4= float(request.form['d'])
       data5= float(request.form['e'])
       data6= float(request.form['f'])
       data7= float(request.form['g'])
       data8= float(request.form['h'])
       data9= int(request.form['i'])
       data10= float(request.form['j'])
       data11= int(request.form['k'])
       data12= int(request.form['l'])
       data13= int(request.form['m'])
       arr=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13])
       pred = model.predict(arr.reshape(1, -1))
       threshold = 0.5
       binary_predictions = np.where(pred >= threshold, 1, 0)
       output={0: "not predicted",1: "predicted"}
       return render_template('index.html',prediction_text='Kidney disease is {}'.format(output[binary_predictions[0]]))
    except Exception as e:
        print("Error:", e)
        return render_template('index.html', prediction_text='Error occurred. Please check your input and try again.')
if __name__=="__main__":
    app.run(debug=True)