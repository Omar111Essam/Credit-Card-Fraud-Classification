# Credit Card Fraud Detection Dashboard

## Overview
An interactive web dashboard for monitoring and analyzing credit card fraud detection metrics, built with Dash and Plotly.

## Features

### 📊 Key Performance Indicators (KPIs)
- Total Transactions
- Fraud Cases Count
- Fraud Rate Percentage
- Average Transaction Amount

### 📈 Visualizations
1. **Transaction Class Distribution** - Bar chart showing normal vs fraud transactions
2. **Transaction Amount Distribution** - Histogram of all transaction amounts
3. **Amount by Transaction Class** - Box plots comparing amounts for normal vs fraud
4. **Time vs Amount Scatter** - Scatter plot showing fraud patterns over time
5. **PCA Feature Analysis** - Interactive feature distribution comparison
6. **Feature Correlation Heatmap** - Correlation matrix of key features
7. **Model Performance Metrics** - Bar chart showing model evaluation metrics

### 🔄 Real-time Updates
- Auto-refreshes every 30 seconds
- Live data from MongoDB Atlas
- Fallback to CSV if database connection fails

## Installation

### Step 1: Install Dependencies
```bash
pip install -r requirements_dashboard.txt
```

Or install individually:
```bash
pip install dash dash-bootstrap-components plotly pandas numpy pymongo dnspython
```

### Step 2: Ensure Data Access
The dashboard will attempt to:
1. Load data from MongoDB Atlas (primary)
2. Fall back to `fraud_data_cloud.csv` if MongoDB is unavailable

Make sure you have either:
- MongoDB Atlas connection configured, OR
- A `fraud_data_cloud.csv` file in the project directory

## Running the Dashboard

### Method 1: Command Line
```bash
python fraud_detection_dashboard.py
```

### Method 2: From Python Script
```python
from fraud_detection_dashboard import app
app.run_server(debug=True, port=8050)
```

### Method 3: From Jupyter Notebook
```python
from fraud_detection_dashboard import app
app.run_server(debug=True, port=8050, mode='inline')
```

## Accessing the Dashboard

Once running, open your web browser and navigate to:
```
http://127.0.0.1:8050
```

## Dashboard Sections

### 1. Header & KPIs
- Overview metrics displayed as cards
- Color-coded for quick identification

### 2. Distribution Visualizations
- Class distribution
- Amount distribution
- Comparative analysis

### 3. Pattern Analysis
- Time-based fraud patterns
- Amount comparisons
- Feature distributions

### 4. Feature Analysis
- Interactive PCA feature selector
- Side-by-side normal vs fraud distributions
- Correlation analysis

### 5. Model Performance
- Custom Random Forest metrics
- Performance comparison charts
- Evaluation scores

## Customization

### Changing Update Interval
Modify the `interval` parameter in the `dcc.Interval` component:
```python
dcc.Interval(
    id='interval-component',
    interval=30*1000,  # Change this value (in milliseconds)
    n_intervals=0
)
```

### Adding New Visualizations
1. Add a new callback function:
```python
@callback(
    Output('new-graph-id', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_new_graph(n):
    # Your visualization code
    return fig
```

2. Add the graph component to the layout:
```python
dcc.Graph(id="new-graph-id")
```

### Changing MongoDB Collection
Modify the collection name in the `get_mongo_data()` function:
```python
collection = db["your_collection_name"]
```

## Troubleshooting

### Dashboard won't start
- Check if port 8050 is already in use
- Verify all dependencies are installed
- Check Python version (3.8+ recommended)

### No data displayed
- Verify MongoDB connection or CSV file exists
- Check data format matches expected structure
- Review console output for error messages

### Slow performance
- Reduce sample size in scatter plots
- Increase update interval
- Consider data caching

## Technical Stack
- **Framework**: Dash (Plotly)
- **Styling**: Bootstrap (via dash-bootstrap-components)
- **Data Source**: MongoDB Atlas / CSV
- **Visualization**: Plotly
- **Language**: Python 3.8+

## Bonus Features Implemented
✅ **Advanced Visualizations** - Multiple interactive charts
✅ **Real-time Monitoring** - Auto-refresh capability
✅ **Data Pipeline Integration** - Direct MongoDB connection
✅ **Performance Optimization** - Efficient data sampling
✅ **Interactive Features** - Dropdown selectors and filters

## Future Enhancements
- [ ] Real-time prediction interface
- [ ] Alert system for high-risk transactions
- [ ] Export functionality for reports
- [ ] User authentication
- [ ] Historical trend analysis
- [ ] Model comparison dashboard

## License
Part of the Credit Card Fraud Classification project.

