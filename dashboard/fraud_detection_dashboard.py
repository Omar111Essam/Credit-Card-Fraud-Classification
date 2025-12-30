"""
Credit Card Fraud Detection Dashboard
Interactive web dashboard for monitoring and analyzing fraud detection metrics
"""

import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc
import sys
import os

# Add parent directory to path to import utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.export_from_mongodb import get_mongo_data

# Load data
print("Loading data from MongoDB...")
df = get_mongo_data()

if df is None:
    # Fallback: try to load from CSV if MongoDB fails
    try:
        # Try project root first, then current directory
        csv_paths = [
            os.path.join(os.path.dirname(__file__), '..', 'fraud_data_cloud.csv'),
            'fraud_data_cloud.csv',
            os.path.join(os.path.dirname(__file__), 'fraud_data_cloud.csv')
        ]
        for csv_path in csv_paths:
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                print(f"Loaded from CSV file: {csv_path}")
                break
        else:
            raise FileNotFoundError("CSV file not found")
    except Exception as e:
        print(f"Error: Could not load data - {e}")
        df = pd.DataFrame()

# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Credit Card Fraud Detection Dashboard"

# Calculate key metrics
if not df.empty:
    total_transactions = len(df)
    fraud_count = df['Class'].sum()
    normal_count = total_transactions - fraud_count
    fraud_rate = (fraud_count / total_transactions) * 100
    avg_amount = df['Amount'].mean()
    fraud_avg_amount = df[df['Class'] == 1]['Amount'].mean()
    normal_avg_amount = df[df['Class'] == 0]['Amount'].mean()
else:
    total_transactions = 0
    fraud_count = 0
    normal_count = 0
    fraud_rate = 0
    avg_amount = 0
    fraud_avg_amount = 0
    normal_avg_amount = 0

# Define app layout
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("💳 Credit Card Fraud Detection Dashboard", 
                   className="text-center mb-4 mt-4",
                   style={'color': '#2c3e50', 'fontWeight': 'bold'}),
            html.P("Real-time monitoring and analytics for fraud detection system",
                   className="text-center text-muted mb-4")
        ])
    ]),
    
    # KPI Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Transactions", className="card-title text-muted"),
                    html.H2(f"{total_transactions:,}", className="text-primary", id="kpi-total"),
                ])
            ], className="mb-4 shadow-sm")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud Cases", className="card-title text-muted"),
                    html.H2(f"{fraud_count:,}", className="text-danger", id="kpi-fraud"),
                ])
            ], className="mb-4 shadow-sm")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Fraud Rate", className="card-title text-muted"),
                    html.H2(f"{fraud_rate:.3f}%", className="text-warning", id="kpi-rate"),
                ])
            ], className="mb-4 shadow-sm")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Avg Amount", className="card-title text-muted"),
                    html.H2(f"${avg_amount:.2f}", className="text-success", id="kpi-amount"),
                ])
            ], className="mb-4 shadow-sm")
        ], width=3),
    ]),
    
    # Main Visualizations Row 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Transaction Class Distribution"),
                dbc.CardBody([
                    dcc.Graph(id="class-distribution")
                ])
            ], className="mb-4 shadow-sm")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Transaction Amount Distribution"),
                dbc.CardBody([
                    dcc.Graph(id="amount-distribution")
                ])
            ], className="mb-4 shadow-sm")
        ], width=6),
    ]),
    
    # Main Visualizations Row 2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Amount by Transaction Class"),
                dbc.CardBody([
                    dcc.Graph(id="amount-by-class")
                ])
            ], className="mb-4 shadow-sm")
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Time vs Amount (Fraud Detection)"),
                dbc.CardBody([
                    dcc.Graph(id="time-amount-scatter")
                ])
            ], className="mb-4 shadow-sm")
        ], width=6),
    ]),
    
    # Feature Analysis
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("PCA Feature Analysis (Top Features)"),
                dbc.CardBody([
                    dcc.Dropdown(
                        id='feature-selector',
                        options=[{'label': f'V{i}', 'value': f'V{i}'} for i in range(1, 11)],
                        value='V1',
                        className="mb-3"
                    ),
                    dcc.Graph(id="feature-distribution")
                ])
            ], className="mb-4 shadow-sm")
        ], width=12),
    ]),
    
    # Correlation Heatmap
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Feature Correlation Heatmap"),
                dbc.CardBody([
                    dcc.Graph(id="correlation-heatmap")
                ])
            ], className="mb-4 shadow-sm")
        ], width=12),
    ]),
    
    # Model Performance Section
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Model Performance Metrics"),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5("Custom Random Forest", className="text-center"),
                            html.Div([
                                html.P("Accuracy: 100%", className="text-success"),
                                html.P("Precision: 82%", className="text-info"),
                                html.P("Recall: 81%", className="text-warning"),
                                html.P("F1-Score: 81%", className="text-primary"),
                                html.P("ROC-AUC: 97.89%", className="text-success"),
                                html.P("PR-AUC: 73.55%", className="text-info"),
                            ], className="text-center")
                        ], width=4),
                        dbc.Col([
                            dcc.Graph(id="model-metrics-chart")
                        ], width=8),
                    ])
                ])
            ], className="mb-4 shadow-sm")
        ], width=12),
    ]),
    
    # Auto-refresh component
    dcc.Interval(
        id='interval-component',
        interval=30*1000,  # Update every 30 seconds
        n_intervals=0
    ),
    
    # Footer
    html.Footer([
        html.Hr(),
        html.P("Credit Card Fraud Detection System | Last Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
               className="text-center text-muted")
    ], className="mt-4 mb-4")
    
], fluid=True)

# Callback for class distribution
@callback(
    Output('class-distribution', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_class_distribution(n):
    if df.empty:
        return go.Figure()
    
    class_counts = df['Class'].value_counts()
    colors = ['#2ecc71', '#e74c3c']
    
    fig = go.Figure(data=[
        go.Bar(
            x=['Normal (0)', 'Fraud (1)'],
            y=[class_counts[0], class_counts[1]],
            marker_color=colors,
            text=[f"{class_counts[0]:,}", f"{class_counts[1]:,}"],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Transaction Class Distribution",
        xaxis_title="Transaction Class",
        yaxis_title="Count",
        template="plotly_white",
        height=400
    )
    
    return fig

# Callback for amount distribution
@callback(
    Output('amount-distribution', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_amount_distribution(n):
    if df.empty:
        return go.Figure()
    
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(
        x=df['Amount'],
        nbinsx=50,
        name='All Transactions',
        marker_color='#3498db',
        opacity=0.7
    ))
    
    fig.update_layout(
        title="Transaction Amount Distribution",
        xaxis_title="Amount ($)",
        yaxis_title="Frequency",
        template="plotly_white",
        height=400
    )
    
    return fig

# Callback for amount by class
@callback(
    Output('amount-by-class', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_amount_by_class(n):
    if df.empty:
        return go.Figure()
    
    fig = go.Figure()
    
    fig.add_trace(go.Box(
        y=df[df['Class'] == 0]['Amount'],
        name='Normal',
        marker_color='#2ecc71'
    ))
    
    fig.add_trace(go.Box(
        y=df[df['Class'] == 1]['Amount'],
        name='Fraud',
        marker_color='#e74c3c'
    ))
    
    fig.update_layout(
        title="Transaction Amount by Class",
        yaxis_title="Amount ($)",
        template="plotly_white",
        height=400,
        showlegend=True
    )
    
    return fig

# Callback for time vs amount scatter
@callback(
    Output('time-amount-scatter', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_time_amount_scatter(n):
    if df.empty:
        return go.Figure()
    
    # Sample data for performance (if dataset is too large)
    sample_size = min(10000, len(df))
    df_sample = df.sample(n=sample_size, random_state=42)
    
    fig = go.Figure()
    
    # Normal transactions
    normal = df_sample[df_sample['Class'] == 0]
    fig.add_trace(go.Scatter(
        x=normal['Time'],
        y=normal['Amount'],
        mode='markers',
        name='Normal',
        marker=dict(color='#2ecc71', size=3, opacity=0.6)
    ))
    
    # Fraud transactions
    fraud = df_sample[df_sample['Class'] == 1]
    fig.add_trace(go.Scatter(
        x=fraud['Time'],
        y=fraud['Amount'],
        mode='markers',
        name='Fraud',
        marker=dict(color='#e74c3c', size=5, opacity=0.8)
    ))
    
    fig.update_layout(
        title="Time vs Amount (Fraud Detection)",
        xaxis_title="Time (seconds)",
        yaxis_title="Amount ($)",
        template="plotly_white",
        height=400
    )
    
    return fig

# Callback for feature distribution
@callback(
    Output('feature-distribution', 'figure'),
    [Input('feature-selector', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_feature_distribution(selected_feature, n):
    if df.empty or selected_feature not in df.columns:
        return go.Figure()
    
    fig = go.Figure()
    
    # Normal transactions
    normal = df[df['Class'] == 0][selected_feature]
    fig.add_trace(go.Histogram(
        x=normal,
        name='Normal',
        marker_color='#2ecc71',
        opacity=0.7,
        nbinsx=50
    ))
    
    # Fraud transactions
    fraud = df[df['Class'] == 1][selected_feature]
    fig.add_trace(go.Histogram(
        x=fraud,
        name='Fraud',
        marker_color='#e74c3c',
        opacity=0.7,
        nbinsx=50
    ))
    
    fig.update_layout(
        title=f"Distribution of {selected_feature} by Class",
        xaxis_title=selected_feature,
        yaxis_title="Frequency",
        template="plotly_white",
        height=400,
        barmode='overlay'
    )
    
    return fig

# Callback for correlation heatmap
@callback(
    Output('correlation-heatmap', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_correlation_heatmap(n):
    if df.empty:
        return go.Figure()
    
    # Select key features for correlation
    key_features = ['Time', 'Amount', 'V1', 'V2', 'V3', 'V4', 'V5', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'Class']
    available_features = [f for f in key_features if f in df.columns]
    
    corr_matrix = df[available_features].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.round(2).values,
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))
    
    fig.update_layout(
        title="Feature Correlation Heatmap",
        template="plotly_white",
        height=600
    )
    
    return fig

# Callback for model metrics chart
@callback(
    Output('model-metrics-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_model_metrics(n):
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC', 'PR-AUC']
    values = [100, 82, 81, 81, 97.89, 73.55]
    colors = ['#2ecc71', '#3498db', '#f39c12', '#9b59b6', '#2ecc71', '#3498db']
    
    fig = go.Figure(data=[
        go.Bar(
            x=metrics,
            y=values,
            marker_color=colors,
            text=[f"{v}%" for v in values],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Model Performance Metrics",
        xaxis_title="Metric",
        yaxis_title="Score (%)",
        yaxis=dict(range=[0, 105]),
        template="plotly_white",
        height=400
    )
    
    return fig

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Starting Fraud Detection Dashboard...")
    print("="*50)
    print(f"📊 Total Transactions: {total_transactions:,}")
    print(f"⚠️  Fraud Cases: {fraud_count:,} ({fraud_rate:.3f}%)")
    print("="*50)
    print("\n🌐 Dashboard running at: http://127.0.0.1:8050")
    print("Press CTRL+C to stop the server\n")
    
    app.run_server(debug=True, port=8050)

