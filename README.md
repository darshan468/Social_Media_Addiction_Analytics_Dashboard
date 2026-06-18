# 📱 Social Media Addiction Analytics Dashboard

## Project Description:
An AI-powered analytics platform designed to identify, monitor, and predict social media addiction risk using Machine Learning, Behavioral Analytics, Explainable AI, Real-Time Monitoring, and Interactive Dashboards.

---
# 1. Project Overview
- End-to-end Data Analytics and Machine Learning solution.
- Analyzes social media behavior patterns.
- Identifies users at risk of addiction.
- Includes Advanced Analytics, Machine Learning, User Segmentation, Anomaly Detection, SHAP Explainability, Real-Time Monitoring, Live Risk Prediction, and an upcoming RAG-based AI Assistant.

# 2. Problem Statement
Explain how excessive social media usage impacts:
- Mental Health
- Sleep Quality
- Productivity
- Academic Performance
- Digital Wellbeing

Mention that traditional analytics only provide descriptive insights while this project provides predictive analytics.

# 3. Dataset Information
Dataset Name:
Social Media User Behavior Dataset

Dataset Size:
- 2000 Users
- 34 Features

# Important Features:
- Age
- Gender
- Country
- Profession
- Daily Usage Hours
- Sessions Per Day
- Average Session Duration
- Followers Count
- Following Count
- Likes Given
- Comments Per Day
- Sleep Disruption
- Mental Health Score
- Notification Frequency
- Mood While Scrolling
- Social Media Breaks

# 4. Technology Stack

Programming:
- Python 3.10+

Data Processing:
- Pandas
- NumPy

Machine Learning:
- Scikit-Learn
- XGBoost
- Isolation Forest
- K-Means Clustering
- SHAP

Visualization:
- Plotly
- Matplotlib

Dashboard:
- Streamlit

Model Deployment:
- Joblib

Version Control:
- Git
- GitHub

# 5. Machine Learning Pipeline

Data Cleaning:
- Missing Value Handling
- Feature Engineering
- Data Transformation
- Risk Score Generation

EDA:
- User Demographics
- Platform Preferences
- Usage Patterns
- Addiction Risk Distribution
- Mental Health Indicators

Feature Engineering:
- Addiction Score
- Sleep Score
- Screen Concern Score
- Break Score

Class Balancing:
- SMOTE

Model Training Results:
Random Forest Accuracy: 87.75%
XGBoost Accuracy: 93.25%

Best Model:
XGBoost Classifier

# 6. Dashboard Features

**Main Dashboard:**
- User Statistics
- Risk Level Distribution
- Platform Usage Analysis
- Daily Usage Patterns
- Correlation Heatmap
- Project Insights

# Machine Learning Insights:
- Model Performance Comparison
- Feature Importance
- Accuracy Metrics
- Business Insights

# User Segmentation:
Using K-Means Clustering

Segments:
- Casual Users
- Active Users
- Heavy Users
- High-Risk Users

# Anomaly Detection:
Using Isolation Forest

Results:
- Normal Users: 1900
- Anomalies: 100

# SHAP Explainability:
Top Features:
1. Daily Usage Hours
2. Average Session Duration
3. Sessions Per Day
4. Sleep Disruption
5. Ad Click Rate

# Real-Time Monitoring:
- Live User Activity
- Usage Trends
- Streamed Records
- Behavioral Changes

# Live AI Predictions:
Risk Levels:
- Low
- Medium
- High
- Severe

# 7. Project Structure

Social Media Addiction Analytics Dashboard
├── Data
│ └── social_media_processed.csv
├── Models
│ └── xgboost_model.pkl
├── Dashboard
│ ├── app.py
│ ├── styles/style.css
│ └── pages
│ ├── 1_Machine_Learning_Insights.py
│ ├── 2_User_Segmentation.py
│ ├── 3_Anomaly_Detection.py
│ ├── 4_SHAP_Insights.py
│ ├── 5_Live_Risk_Prediction.py
│ └── 6_Real_Time_Monitoring.py
├── Streaming
│ └── live_predictions.csv
├── requirements.txt
└── README.md

# 8. Installation Guide

Clone Repository:
git clone https://github.com/yourusername/social-media-addiction-dashboard.git

Install Dependencies:
pip install -r requirements.txt

Run:
streamlit run Dashboard/app.py

9. Key Results

Users Analyzed:
2000

Average Usage:
2.99 Hours/Day

Average Addiction Score:
24.8

Model Accuracy:
93.25%

High-Risk Users:
85+

# 10. Future Enhancements

- RAG-Based AI Assistant
- Conversational Analytics Chatbot
- LLM Integration
- Real-Time API Streaming
- Cloud Deployment
- User Recommendation Engine
- Wellness Intervention Suggestions

## Developer Section

Name:
Darshan S

Education:
Artificial Intelligence & Data Science Student

College:
Prathyusha Engineering College

Role:
Aspiring Data Analyst | Machine Learning Enthusiast | AI Developer

# License

MIT License
