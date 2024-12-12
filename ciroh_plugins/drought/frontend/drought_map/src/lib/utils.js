async function getDroughtDates() {
    const api_endpoint = 'https://droughtmonitor.unl.edu/Maps/CompareTwoWeeks.aspx/ReturnDates';
    const response = await fetch(api_endpoint, {
      headers: { "Content-Type": "application/json" }
    });
    
    const data = await response.json();
    
    // Structure matches what the Python code returns
    const dropdown_items = [
      {
        label: "Drought Dates",
        options: (data.d || []).map(item => ({
          value: String(item.Value),
          label: item.Text
        }))
      }
    ];
  
    return dropdown_items;
  }

export { getDroughtDates };