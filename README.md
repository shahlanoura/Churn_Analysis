# Customer Churn Analysis

This project predicts customer churn probability based on user input. The application is built using **Flask** and a pre-trained machine learning model, and it provides an easy-to-use web interface for predictions.

## Features
- Predict customer churn probability using a trained model.
- Simple and interactive web interface for inputting customer data.
- JSON response with churn probability and status.

## Tech Stack
- **Flask**: Web framework for building the application.
- **scikit-learn**: Used for training the churn prediction model.
- **Joblib**: For saving and loading the trained model.
- **HTML** and **CSS**: For creating the web interface.

## Project Structure
```plaintext
Churn_Analysis/
│
├── templates/
│   ├── index.html       
│
├── venv/                
│
├── churn_model.joblib     
├── main.py              
├── requirements.txt     
└── README.md      

Installation
      
git clone https://github.com/your-username/Churn_Analysis.git
cd Churn_Analysis
create virtualEnv
python -m venv venv
source venv/bin/activate
Pip install
pip install -r requirements.txt
python main.py

Example input
{MonthlyCharges: 50.00
TotalCharges: 1200.00
ServiceUsage1: 5
ServiceUsage2: 3
ServiceUsage3: 7
Payment_BankTransfer: 1
Payment_Cash: 0
Payment_CreditCard: 0
Payment_PayPal: 0
AvgSpendPerMonth: 100.00}

Output:-
{
  "Churn_Probability": 0.65,
  "Message": "Prediction successful"
}
