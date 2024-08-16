from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import traceback
import pickle


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = (
        "<h3>Sklearn Prediction Loan: From Azure Pipelines (Continuous Delivery)</h3>"
    )
    return html.format(format)


# TO DO:  Log out the prediction values
@app.route("/predict", methods=["POST"])
def predict():
    """Performs an sklearn prediction

    input looks like:
        {
            Gender: Male,
            Married: Unmarried,
            Credit_History: Uncleared Debts,
            ApplicantIncome: 1000,
            LoanAmount: 240000
    }
    result looks like:
    { "prediction": [0] }

    """

    try:
        clf = pickle.load(open("classifier.pkl","rb"))
    except Exception as e:
        LOG.error("Error loading model: %s", str(e))
        LOG.error("Exception traceback: %s", traceback.format_exc())
        return "Model not loaded"
    
    json_payload = request.json
    LOG.info("JSON payload: %s{data}".format(data=json_payload))
    if json_payload['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if json_payload['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if json_payload['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  

    ApplicantIncome = json_payload['ApplicantIncome']
    LoanAmount = json_payload['LoanAmount']
    prediction = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return jsonify({"prediction": pred})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
