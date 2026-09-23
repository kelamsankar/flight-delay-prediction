# ✈️ Flight Delay Prediction System

An end-to-end **Flight Delay Prediction System** built using **Python, SQL, XGBoost, and Streamlit** to analyze historical flight data and predict the probability of flight delays.

## 📌 Overview

This project follows a complete machine learning workflow:

**Data Cleaning → EDA → SQL Analysis → Feature Engineering → Model Training → Model Evaluation → Threshold Tuning → Streamlit Deployment**

The system predicts whether a flight is likely to be:

* 🔴 **Delayed**
* 🟢 **Not Delayed**

The application also displays the estimated **delay probability** and the model's **55% decision threshold**.

---

## 🛠️ Technologies

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **XGBoost**
* **SQL / SQLite**
* **Matplotlib & Seaborn**
* **Streamlit**
* **Jupyter Notebook**
* **Git & GitHub**

---

## 📂 Project Structure

```text
flight-delay-prediction/
│
├── app/
│   ├── app.py
│   └── predict.py
│
├── data/
│   ├── airline_delay_analysis.csv
│   ├── cleaned_flights.csv
│   ├── flights.db
│   ├── flights_sample.csv
│   ├── hour_delay_analysis.csv
│   ├── month_delay_analysis.csv
│   └── route_delay_analysis.csv
│
├── models/
│   ├── category_mappings.pkl
│   ├── flight_delay_xgboost.pkl
│   └── threshold.pkl
│
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_sql_analysis.ipynb
│   └── 03_model_training.ipynb
│
├── screenshots/
│   ├── 01_main_application.png
│   ├── 02_delayed_prediction.png
│   ├── 03_prediction.png
│   └── 04_early_morning.png
│
├── run_app.sh
├── .gitignore
└── README.md
```

---

## 🔍 Data Analysis

The project includes:

* Data cleaning and preprocessing
* Missing-value analysis
* Exploratory Data Analysis
* Airline delay analysis
* Monthly delay analysis
* Hourly delay analysis
* Route-level delay analysis
* SQLite-based SQL analysis

---

## 🤖 Machine Learning

Several classification models were evaluated, including:

* Logistic Regression
* Random Forest
* XGBoost
* Balanced XGBoost
* Tuned XGBoost

The final model uses **XGBoost** with class-imbalance handling.

The model uses:

* Airline
* Origin Airport
* Destination Airport
* Month
* Day
* Day of Week
* Departure Hour
* Scheduled Time
* Distance
* Weekend Indicator

### Class Imbalance

The dataset contains more non-delayed flights than delayed flights.

XGBoost was configured with:

```text
scale_pos_weight = 4.4187
```

to give greater importance to the delayed-flight class.

---

## 🎚️ Prediction Threshold

The classification threshold was tuned using multiple probability thresholds.

The selected threshold is:

```text
55%
```

Therefore:

```text
Delay Probability >= 55%
        ↓
     DELAYED

Delay Probability < 55%
        ↓
   NOT DELAYED
```

---

## 📊 Model Performance

Final test-set performance:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **71.56%** |
| Precision | **33.70%** |
| Recall    | **55.96%** |
| F1 Score  | **42.07%** |
| ROC-AUC   | **71.75%** |

---

## 🌐 Streamlit Application

The application allows users to enter:

* Airline code
* Origin airport
* Destination airport
* Month
* Day
* Day of week
* Departure hour
* Scheduled time
* Distance
* Weekend indicator

The application displays:

* Flight delay prediction
* Delay probability
* Risk level
* Decision threshold

### Example

```text
Airline: DL
Origin: ATL
Destination: JFK
Month: 1
Day: 3
Day of Week: 6
Departure Hour: 10
Scheduled Time: 130
Distance: 760
Weekend: Yes
```

Example result:

```text
Prediction: DELAYED
Delay Probability: 61.09%
Decision Threshold: 55%
```

---

## 📸 Screenshots

### Main Application

![Main Application](screenshots/01_main_application.png)

### Delayed Prediction

![Delayed Prediction](screenshots/02_delayed_prediction.png)

### Prediction Result

![Prediction Result](screenshots/03_prediction.png)

### Early Morning Prediction

![Early Morning Prediction](screenshots/04_early_morning.png)

---

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/kelamsankar/flight-delay-prediction.git
cd flight-delay-prediction
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost streamlit joblib matplotlib seaborn
```

Run the application:

```bash
python3 -m streamlit run app/app.py
```

Or:

```bash
./run_app.sh
```

---

## 📓 Notebooks

### `01_data_cleaning_eda.ipynb`

Data cleaning, preprocessing, and exploratory data analysis.

### `02_sql_analysis.ipynb`

SQL/SQLite analysis of airline, hourly, monthly, and route-level delays.

### `03_model_training.ipynb`

Model training, evaluation, class-imbalance handling, threshold tuning, and model saving.

---

## 🚀 Future Improvements

* Real-time flight information
* Weather-data integration
* SHAP-based model explainability
* Online deployment
* Automated model retraining
* Prediction history and monitoring dashboard

---

## 👨‍💻 Author

**Sankar**

B.Tech Computer Science & Engineering Student

Interested in **Data Science, Machine Learning, Artificial Intelligence, and Generative AI**.

---

⭐ **Flight Delay Prediction System — End-to-End Machine Learning Project**
