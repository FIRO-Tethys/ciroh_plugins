import React from 'react';
import DataTable from 'react-data-table-component';
import './index.css';

const customStyles = ({
  pagination: {
    style: {
      overflow: "hidden",
    }
  }
})
const header_name = {
  D0: 'D0-D4',
  D1: 'D1-D4',
  D2: 'D2-D4',
  D3: 'D3-D4',
  D4: 'D4',
  DSCI: 'DSCI',
  None: 'None',
}
const TableComponent = ({ data }) => {
  const formatedColumns = [
    {
      name: 'Week',
      selector: row => row.Date,
      sortable: true,
      id: 'Week',
    },
    ...(data.length > 0
      ? Object.keys(data[0])
          .filter(key => !['Label', '__type', 'Date'].includes(key))
          .map(configName => {
            return {
              name: header_name[configName],
              id: configName,
              selector: row => row[configName],
              sortable: true,
            };
          })
      : []
    )
  ];

  return (
    <div className="table-wrapper-custom">
      <DataTable
        columns={formatedColumns}
        customStyles={customStyles}
        data={data}
        pagination
        defaultSortField="Week"
      />
    </div>
  );
};

export default TableComponent;