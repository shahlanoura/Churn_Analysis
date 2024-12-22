from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Load the pre-trained churn prediction model
try:
    model = pickle.load(open("churn_model.pkl", "rb"))
except FileNotFoundError:
    raise Exception("The churn_model.pkl file was not found. Please ensure it is in the correct directory.")

# Initialize Flask app
main = Flask(__name__)

# Route for the home page
@main.route('/')
def index():
    return render_template('index.html')

# Route for prediction
@main.route('/predict', methods=['POST'])
def predict_churn():
    try:
        # Extract input data from the form
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

        # Convert inputs to float
        input_array = np.array(input_features, dtype=float).reshape(1, -1)

        # Predict churn probability
        probability = model.predict_proba(input_array)[0][1]

        # Return results
        return jsonify({
            "Churn_Probability": probability,
            "Message": "Prediction successful"
        })
    except Exception as e:
        return jsonify({
            "Error": str(e),
            "Message": "An error occurred during prediction"
        }), 400

if __name__ == "__main__":
    # Run the app locally
    main.run(debug=True)
