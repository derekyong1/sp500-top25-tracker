from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    api_key = "05166bc463a471432f1ff89803b15568"
    url = f"https://financialmodelingprep.com/api/v3/profile/AAPL,GOOGL,MSFT?apikey={api_key}"  # Example URL
    response = requests.get(url)
    data = response.json()
    print(data)
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Assuming the API returns market cap, sort by 'marketCap' and select top 25 companies
    # Note: Adjust the field name 'marketCap' based on actual response
    top_companies = df.sort_values(by='mktCap', ascending=False).head(25)

    return render_template('index.html', companies=top_companies.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
