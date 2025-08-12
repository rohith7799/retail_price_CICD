# x = data[['qty', 'unit_price', 'comp_1', 'product_score', 'comp_price_diff']]

# y = data['total_price']

import pickle
import numpy as np

# Load the model
with open("decision_tree_model.pkl", 'rb') as file:
    dt_model = pickle.load(file)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to the Homepage of Retail Price Optimization Project"

@app.route('/project', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Get input values from the form
        qty = float(request.form['qty'])
        unit_price = float(request.form['unit_price'])
        comp_1 = float(request.form['comp_1'])
        product_score = float(request.form['product_score'])

        # Create input array (assuming model expects 5 features including comp_price_diff)
        # If comp_price_diff is excluded, remove it from model training or add logic here.
        # Here we'll assume it is calculated as:
        comp_price_diff = unit_price - comp_1

        input_data = np.array([[qty, unit_price, comp_1, product_score, comp_price_diff]])

# Make prediction
        prediction = dt_model.predict(input_data)[0]
        prediction = round(prediction, 2)

        # Render the same form with prediction result
        return render_template('index.html', prediction=prediction)

        
# the file index.html contains the code for displaying the form

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)    # default host = 127.0.0.1 and port = 5000

# to create docker image cmd = docker build -t rohithkumar124/retail_app
# to run container cmd = docker run -p 5000:5000 rohithkumar124/retail_app
# to push image to docker hub cmd = docker push rohithkumar124/retail_app
# to create a github repository and push all files to github repo, follow below steps
# git init
# git add .
# git commit -m "any comment"
# gh repo create repo_name --public --source=. --remote=origin --push