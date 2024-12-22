from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Load the pre-trained churn prediction model
model = pickle.load(open("churn_model.pkl", "rb"))

main = Flask(__name__)

# Route for the form
@main.route('/')
def index():
    return render_template('index.html')

# Route for prediction
@main.route('/predict', methods=['POST'])
def predict_churn():
    # Get input data from the form
    input_features = [
       
        request.form.get('MonthlyCharges', 0),
        request.form.get('TotalCharges', 0),
        request.form.get('ServiceUsage1', 0),
        request.form.get('ServiceUsage2', 0),
        request.form.get('ServiceUsage3', 0),
        request.form.get('Payment_BankTransfer', 0),
        request.form.get('Payment_Cash', 0),
        request.form.get('Payment_CreditCard', 0),
        request.form.get('Payment_PayPal', 0),
        request.form.get('AvgSpendPerMonth', 0)
    ]

    # Preprocess the input (scaling, etc.)
    input_array = np.array(input_features, dtype=float).reshape(1, -1)
    
    # Predict churn probability
    probability = model.predict_proba(input_array)[0][1]

    # Display the result on the webpage
    return jsonify({
        "Churn_Probability": probability,
        "Message": "Prediction successful"
    })

if __name__ == "__main__":
    pass
