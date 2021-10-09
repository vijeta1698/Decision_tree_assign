import pickle
from flask import Flask,render_template,request

model = pickle.load(open("titanicModel1.pickle",'rb'))
print(model.predict([[6,0,1,33,1,0,0]])[0])

app = Flask(__name__)
@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    Age = request.form['txtAge']
    sibsp = request.form['txtSibsp']
    parch = request.form['txtParch']
    fare = request.form['txtFare']
    pclass = request.form['txtPclass_2']
    #pclass3 = request.form['txtPclass_3']
    sex = request.form['txtSex']
    if pclass == '1':
        print("in 1")
        predict = model.predict([[Age,sibsp,parch,fare,0,0,sex]])
        if predict[0] == 0:
            return render_template('index.html',prediction_text = "Sorry!! The passenger couldnt survive")
        else:
            return render_template('index.html',prediction_text = 'Passenger Survived')
    elif pclass=='2':
        print("in 2")
        predict = model.predict([[Age, sibsp, parch, fare, 1, 0, sex]])
        if predict[0] == 0:
            return render_template('index.html',prediction_text="Sorry!! The passenger couldnt survive")
        else:
            return render_template('index.html', prediction_text='Passenger Survived')
    elif pclass=='3':
        print("in 3")
        predict = model.predict([[Age, sibsp, parch, fare, 0, 1, sex]])
        if predict[0] == 0:
            return render_template('index.html',prediction_text="Sorry!! The passenger couldnt survive")
        else:
            return render_template('index.html', prediction_text='Passenger Survived')



if __name__ == '__main__':
    app.run()