import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.metrics import accuracy_score
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder = 'templates')
q = ""


@app.route("/")
def LoadPage():
    return render_template('home.html', query="")

@app.route("/", methods=['POST'])
def customerPrediction():
    df_with_clusters = pd.read_csv('Customer Data with clusters.csv')

    
    try:
        inputQuery1 = float(request.form['query1'])
        inputQuery2 = float(request.form['query2'])
        inputQuery3 = float(request.form['query3'])
        inputQuery4 = float(request.form['query4'])
        inputQuery5 = float(request.form['query5'])
        inputQuery6 = float(request.form['query6'])
        inputQuery7 = float(request.form['query7'])
        inputQuery8 = float(request.form['query8'])
        inputQuery9 = float(request.form['query9'])
        inputQuery10 = float(request.form['query10'])
        inputQuery11 = float(request.form['query11'])
        inputQuery12 = float(request.form['query12'])
        inputQuery13 = float(request.form['query13'])
        inputQuery14 = float(request.form['query14'])
        inputQuery15 = float(request.form['query15'])
        inputQuery16 = float(request.form['query16'])
        inputQuery17 = float(request.form['query17'])
    except ValueError:
        return "Invalid input. Please enter numeric values for all fields."


# if retrain every time 
    #X = df_with_clusters.drop(columns=['Cluster'])  # Features
    #y = df_with_clusters['Cluster']  # Target variable

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #decision_tree = DecisionTreeClassifier(random_state=42)
    #decision_tree.fit(X_train, y_train)
    #y_pred = decision_tree.predict(X_test)
    #accuracy = accuracy_score(y_test, y_pred)
    #print("Accuracy:", accuracy)   

    model = pickle.load(open("decision_tree_model.pkl", "rb"))

    data = [[inputQuery1,inputQuery2,inputQuery3,inputQuery4,inputQuery5,inputQuery6,inputQuery7,inputQuery8,inputQuery9,inputQuery10,inputQuery11,inputQuery12,inputQuery13,inputQuery14,inputQuery15,inputQuery16,inputQuery17]]

    new_df = pd.DataFrame(data, columns = ['BALANCE','BALANCE_FREQUENCY','PURCHASES','ONEOFF_PURCHASES','INSTALLMENTS_PURCHASES','CASH_ADVANCE','PURCHASES_FREQUENCY','ONEOFF_PURCHASES_FREQUENCY','PURCHASES_INSTALLMENTS_FREQUENCY','CASH_ADVANCE_FREQUENCY','CASH_ADVANCE_TRX','PURCHASES_TRX','CREDIT_LIMIT','PAYMENTS','MINIMUM_PAYMENTS','PRC_FULL_PAYMENT','TENURE'])

    single = model.predict(new_df)

    if single==0:
        o1 = "The customer belongs to Cluster 0: Responsible Spenders" 
    elif single== 1:
       o1 = "The customer belongs to Cluster 1: Big Spenders"
    elif single== 2:
       o1 = "The customer belongs to Cluster 2: Conservative Spenders"
    else:
        o1 = "The customer belongs to Cluster 3: Elite Spenders"

    return render_template ('home.html', output1 = o1,query1 = request.form['query1'],query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'],query11 = request.form['query11'],query12 = request.form['query12'],query13 = request.form['query13'],query14 = request.form['query14'],query15 = request.form['query15'],query16 = request.form['query16'],query17 = request.form['query17'])

app.run(port=8000)