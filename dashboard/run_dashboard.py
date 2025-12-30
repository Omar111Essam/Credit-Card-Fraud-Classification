"""
Simple script to run the Fraud Detection Dashboard
"""

import sys
import os

# Add dashboard directory to path
dashboard_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dashboard_dir)

try:
    from fraud_detection_dashboard import app
    
    if __name__ == '__main__':
        print("\n" + "="*60)
        print("🚀 Starting Credit Card Fraud Detection Dashboard")
        print("="*60)
        print("\n📋 Dashboard Features:")
        print("   • Real-time KPI monitoring")
        print("   • Interactive visualizations")
        print("   • Model performance metrics")
        print("   • Feature analysis tools")
        print("\n🌐 Access the dashboard at: http://127.0.0.1:8050")
        print("   Press CTRL+C to stop the server\n")
        print("="*60 + "\n")
        
        app.run(debug=True, port=8050, host='127.0.0.1')
        
except ImportError as e:
    print("❌ Error: Missing dependencies")
    print(f"   {e}")
    print("\n💡 Install dependencies with:")
    print("   pip install -r requirements.txt")
    print("   or")
    print(f"   pip install -r {os.path.join(dashboard_dir, 'requirements_dashboard.txt')}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting dashboard: {e}")
    sys.exit(1)

