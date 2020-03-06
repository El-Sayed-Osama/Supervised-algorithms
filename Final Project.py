#GUI Import
from flask import Flask,render_template,request
app = Flask(__name__)
########
from sklearn.naive_bayes import GaussianNB #Naive Base
from sklearn.neural_network import MLPClassifier #Nueral Network
from sklearn.svm import SVC #Support Vector Machine
from sklearn.tree import DecisionTreeClassifier #Tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
#Read Excel File date
def readdata():
    l=[0,0]
    data = pd.read_excel('D:\My Projects\Machine Learning\Project\Project.xlsx')
    df = pd.DataFrame(data)
    y = df['is_legendary']
    x = df.drop(['is_legendary'], axis=1)
    l=[x,y]
    return l
#SV
def sv(data):
    x=data[0]
    y=data[1]
    clf = SVC(kernel='rbf',gamma='auto')
    clf.fit(x,y)
    y_pred=clf.predict(x)
    return round(accuracy_score(y, y_pred),2)
#NB
def nb(data):
    x=data[0]
    y=data[1]
    clf = GaussianNB()
    clf.fit(x,y)
    y_pred = clf.predict(x)
    return round(accuracy_score(y, y_pred),2)
#NN
def nn(data):
    x=data[0]
    y=data[1]
    x_trian,x_test,y_train,y_test=train_test_split(x,y)
    clf=MLPClassifier(hidden_layer_sizes=(9,10))
    clf.fit(x_trian,y_train)
    y_pred=clf.predict(x_test)
    return round(accuracy_score(y_test,y_pred),2)
#DT
def TREE(data):
    x=data[0]
    y=data[1]
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(x,y)
    y_pred = clf.predict(x)
    return round(accuracy_score(y, y_pred),2)

##########################################################
@app.route('/')
def index():
    return render_template('s.html')
##########################################################
@app.route('/form', methods=['GET','POST'])
def form():
    if 'svc' in request.form:
        if request.method=='POST':
            data=readdata()
            res=sv(data)
            return render_template('s.html',x=res)
        else:
            return render_template('s.html')
    elif 'nn' in request.form:
        if request.method=='POST':
            data=readdata()
            res=nn(data)
            return render_template('s.html',y=res)
        else:
            return render_template('s.html')
    elif 'nb' in request.form:
        if request.method=='POST':
            data=readdata()
            res=nb(data)
            return render_template('s.html',z=res)
        else:
            return render_template('s.html')
    elif 'dt' in request.form:
        if request.method=='POST':
            data=readdata()
            res=TREE(data)
            return render_template('s.html',c=res)
        else:
            return render_template('s.html')
    else:
        if request.method=='POST':
            data=readdata()
            x=data[0]
            y=data[1]
            df = pd.DataFrame(x)
            abil = df['abilities']
            clasi = df['classfication']
            name = df['name']
            gen = df['generation']
            return render_template('info.html',x=abil,y=clasi,z=name,w=gen)
        else:
            return render_template('s.html')

###################################################
if __name__ == '__main__':
    app.run(debug = True)