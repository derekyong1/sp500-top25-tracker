import React, { useEffect, useState } from 'react';
import CompanyList from './CompanyList';

function App() {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/companies')
      .then(response => response.json())
      .then(data => setCompanies(data))
      .catch(error => console.error("Failed to fetch companies", error));
  }, []);

  return (
    <div className="App">
      <h1>Top 25 S&P 500 Companies by Market Cap</h1>
      <CompanyList companies={companies} />
    </div>
  );
}

export default App;
