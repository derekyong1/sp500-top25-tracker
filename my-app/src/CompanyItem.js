function CompanyItem({ companyName, symbol, mktCap }) {
    return (
      <li>
        {companyName} ({symbol}): ${mktCap}
      </li>
    );
  }
  
  export default CompanyItem;
  