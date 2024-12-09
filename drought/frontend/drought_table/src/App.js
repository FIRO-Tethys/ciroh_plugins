import React from "react";
import DataTable from 'react-data-table-component';

import "./index.css";

const TableComponent = (
  {
    data
  }

) => {
  const formatedColumns = [
    { name: 'Week', selector: row => row.Date, sortable: true },
    ...(data.length > 0
        ? Object.keys(data[0])
              .filter(key => key !== 'Label')
              .filter(key => key !== '__type')
              .filter(key => key !== 'Date')
              .map(configName => ({
                  name: configName,
                  selector: row => row[configName],
                  sortable: true,
              }))
        : []),
];

  return (
    <DataTable
      columns={formatedColumns}
      data={data}
    />
  );
  
}

export default TableComponent;