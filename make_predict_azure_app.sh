#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
  "Gender": "Male",
  "Married": "Married",
  "ApplicantIncome": 13000,
  "LoanAmount": 30000, 
  "Credit_History":"Non default"
}'\
     -H "Content-Type: application/json" \
     -X POST https://azuredemomlapp.azurewebsites.net:$PORT/predict 
     #your application name <yourappname>goes here