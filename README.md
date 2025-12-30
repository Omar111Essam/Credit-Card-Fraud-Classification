# Credit Card Fraud Classification

A comprehensive machine learning project for detecting credit card fraud using big data techniques, custom Random Forest implementation, and interactive dashboards.

## 📁 Project Structure

```
Credit-Card-Fraud-Classification/
├── notebooks/          # Jupyter notebooks for EDA and modeling
├── dashboard/          # Interactive web dashboard
├── utils/              # Utility functions (data loading, etc.)
├── docs/               # Additional documentation
└── requirements.txt    # Project dependencies
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed structure documentation.

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd Credit-Card-Fraud-Classification

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Access

The project uses MongoDB Atlas for data storage. Ensure you have:

- MongoDB Atlas connection configured in `utils/export_from_mongodb.py`
- Or a local `fraud_data_cloud.csv` file in the project root

### 3. Running Analysis

#### Jupyter Notebooks

```bash
cd notebooks
jupyter notebook
```

#### Interactive Dashboard

```bash
python dashboard/run_dashboard.py
```

Then open your browser to: `http://127.0.0.1:8050`

## 📊 Project Components

### 1. Exploratory Data Analysis (EDA)

- **Notebook 1**: Data understanding and quality assessment
- **Notebook 2**: Visualization and insights
- Identifies class imbalance, feature distributions, and patterns

### 2. Custom Random Forest Model

- Custom implementation of Random Forest classifier
- Bootstrap aggregation and feature randomness
- Handles class imbalance with balanced class weights
- Performance metrics: 100% accuracy, 82% precision, 81% recall

### 3. Interactive Dashboard (Bonus)

- Real-time KPI monitoring
- Interactive visualizations
- Model performance metrics
- Feature analysis tools
- Auto-refresh every 30 seconds

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Machine learning utilities
- **MongoDB Atlas**: Cloud database
- **Dash & Plotly**: Interactive dashboard
- **Jupyter**: Notebook environment

## 📈 Key Features

- ✅ Big Data processing with MongoDB Atlas
- ✅ Custom Random Forest implementation
- ✅ Comprehensive EDA with visualizations
- ✅ Interactive web dashboard
- ✅ Modular, clean code structure
- ✅ Real-time monitoring capabilities

## 📝 Notebooks

1. **01_EDA_Data_Understanding_Quality.ipynb**

   - Dataset loading and inspection
   - Missing values and duplicate detection
   - Statistical summaries
   - Data quality assessment

2. **02_EDA_Insights_Visualization.ipynb**

   - Class distribution analysis
   - Transaction amount distributions
   - Correlation analysis
   - PCA feature comparisons
   - Interactive dashboard integration

3. **03_BigData_Fraud_Detection.ipynb**
   - Custom Random Forest implementation
   - Model training and evaluation
   - Performance metrics
   - Hyperparameter tuning

## 🎯 Model Performance

- **Accuracy**: 100%
- **Precision**: 82%
- **Recall**: 81%
- **F1-Score**: 81%
- **ROC-AUC**: 97.89%
- **PR-AUC**: 73.55%

## 📚 Documentation

- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Detailed project structure
- [dashboard/README.md](dashboard/README.md) - Dashboard documentation

## 🔧 Utilities

### Data Loading

```python
from utils.export_from_mongodb import get_mongo_data

df = get_mongo_data()
```

## 🎁 Bonus Features

- **Advanced Visualizations**: Multiple interactive charts
- **Real-time Monitoring**: Auto-refresh dashboard
- **Data Pipeline Integration**: Direct MongoDB connection
- **Performance Optimization**: Efficient data sampling
- **Modular Architecture**: Clean, organized code structure

## 📄 License

This project is part of a university coursework assignment.

## 👥 Contributors

University project team

---

For more details, see the individual component documentation in their respective directories.
