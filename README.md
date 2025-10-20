# ✈️ Flight Price Prediction

**Predict flight prices, practise feature engineering, and implement ensemble models.**

---

## 📘 About the Dataset

### 🧭 Introduction
The objective of this project is to analyze a **flight booking dataset** obtained from the **EaseMyTrip** website and to conduct statistical analysis to extract meaningful insights.  
A **Linear Regression** model will be used to predict a continuous target variable — the **flight price**.

EaseMyTrip is an online platform for booking flight tickets. By studying this dataset, we can uncover valuable insights for both passengers and airline stakeholders.

---

## 🎯 Research Questions

This study aims to answer the following questions:

1. Does the price vary with airlines?  
2. How is the price affected when tickets are bought just 1 or 2 days before departure?  
3. Does ticket price change based on departure and arrival time?  
4. How does the price change with the source and destination cities?  
5. How does the ticket price vary between Economy and Business class?

---

## 🧪 Data Collection and Methodology

Data was extracted from **EaseMyTrip** using the **Octoparse web scraping tool**.

- **Timeframe:** February 11th – March 31st, 2022  
- **Total Records:** 300,261 flight booking options  
- **Classes:** Economy and Business  
- **Data Type:** Secondary data  

---

## 📊 Dataset Overview

The dataset contains information about flight booking options for flights between India’s **top 6 metro cities**.

- **Total records:** 300,261  
- **Total features:** 11  

### ✨ Features Description

| Feature | Type | Description |
|----------|------|-------------|
| **Airline** | Categorical | Name of the airline company (6 unique airlines) |
| **Flight** | Categorical | Flight code identifier |
| **Source City** | Categorical | City where the flight takes off (6 unique cities) |
| **Departure Time** | Categorical | Grouped time period for departure (6 unique bins) |
| **Stops** | Categorical | Number of stops (3 distinct values) |
| **Arrival Time** | Categorical | Grouped time period for arrival (6 unique bins) |
| **Destination City** | Categorical | City where the flight lands (6 unique cities) |
| **Class** | Categorical | Seat class (Business / Economy) |
| **Duration** | Numerical | Total travel time (in hours) |
| **Days Left** | Numerical | Days between booking date and travel date |
| **Price** | Numerical | Target variable – ticket price |

---

## 🧠 Project Goal

Build an **end-to-end machine learning pipeline** for flight price prediction:
- Data exploration and visualization  
- Feature engineering and preprocessing  
- Model training and evaluation  
- Hyperparameter tuning  
- Deployment-ready model saving  

---

## 📂 Dataset Source

🔗 [Kaggle: Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

---

> 💡 *To boost learning, try building a complete end-to-end project using this dataset.*