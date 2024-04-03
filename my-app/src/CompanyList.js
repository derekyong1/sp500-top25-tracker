import CompanyItem from './CompanyItem';

function CompanyList({ companies }) {
  return (
    <ol>
      {companies.map(company => (
        <CompanyItem key={company.symbol} {...company} />
      ))}
    </ol>
  );
}

export default CompanyList;
