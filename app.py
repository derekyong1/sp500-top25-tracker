# Module imports
from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS
from urllib.parse import quote
import requests
import pandas as pd

# Function imports
from company_list import get_top_companies as companies

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def serve():
#     return send_from_directory(app.static_folder, 'index.html')


@app.route('/companies', methods=["GET", "POST"])
def get_companies():
    api_key = "05166bc463a471432f1ff89803b15568"

    all_data = []
    company_identifiers = companies()
    for i in range(len(company_identifiers)):
        url = f"https://financialmodelingprep.com/api/v3/profile/{company_identifiers[i]}?apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        all_data.extend(data)

    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Assuming the API returns market cap, sort by 'marketCap' and select top 25 companies
    # Note: Adjust the field name 'marketCap' based on actual response
    top_companies = df.sort_values(by='mktCap', ascending=False).head(25)

    # Converts into a dictionary to be turned into a JSON format
    result = jsonify(top_companies.to_dict('records'))
    return result


if __name__ == '__main__':
    app.run(debug=True)
