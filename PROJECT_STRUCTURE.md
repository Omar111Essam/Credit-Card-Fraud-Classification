# Project Structure

This document describes the organization of the Credit Card Fraud Classification project.

## Directory Structure

```
Credit-Card-Fraud-Classification/
│
├── notebooks/                          # Jupyter notebooks for analysis
│   ├── 01_EDA_Data_Understanding_Quality.ipynb
│   ├── 02_EDA_Insights_Visualization.ipynb
│   └── 03_BigData_Fraud_Detection.ipynb
│
├── dashboard/                          # Interactive dashboard application
│   ├── __init__.py
│   ├── fraud_detection_dashboard.py   # Main dashboard application
│   ├── run_dashboard.py               # Dashboard launcher script
│   ├── requirements_dashboard.txt      # Dashboard-specific dependencies
│   └── README.md                      # Dashboard documentation
│
├── utils/                              # Utility functions and scripts
│   ├── __init__.py
│   └── export_from_mongodb.py         # MongoDB data loading utility
│
├── docs/                               # Additional documentation
│
├── requirements.txt                    # Project dependencies
├── README.md                           # Main project README
└── PROJECT_STRUCTURE.md               # This file
```

## Module Descriptions

### `notebooks/`
Contains all Jupyter notebooks for exploratory data analysis, visualization, and model development:
- **01_EDA_Data_Understanding_Quality.ipynb**: Initial data exploration and quality assessment
- **02_EDA_Insights_Visualization.ipynb**: Visual analysis and pattern identification
- **03_BigData_Fraud_Detection.ipynb**: Custom Random Forest implementation and model training

### `dashboard/`
Interactive web dashboard built with Dash and Plotly:
- **fraud_detection_dashboard.py**: Main dashboard application with visualizations
- **run_dashboard.py**: Simple launcher script
- **README.md**: Dashboard-specific documentation

### `utils/`
Reusable utility functions:
- **export_from_mongodb.py**: Function to load data from MongoDB Atlas

## Usage

### Running Notebooks
```bash
cd notebooks
jupyter notebook
```

### Running Dashboard
```bash
# From project root
python dashboard/run_dashboard.py

# Or from dashboard directory
cd dashboard
python run_dashboard.py
```

### Using Utilities
```python
from utils.export_from_mongodb import get_mongo_data

df = get_mongo_data()
```

## Import Paths

When importing modules from different directories:

```python
# From notebooks or root scripts
from utils.export_from_mongodb import get_mongo_data

# From dashboard
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.export_from_mongodb import get_mongo_data
```

## Data Files

Data files (CSV, etc.) should be placed in the project root directory for easy access from all modules.

## Best Practices

1. **Modularity**: Keep related code in appropriate directories
2. **Reusability**: Place common functions in `utils/`
3. **Documentation**: Update this file when adding new modules
4. **Dependencies**: Add new requirements to `requirements.txt`

