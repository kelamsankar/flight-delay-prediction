# flight-delay-prediction
An end-to-end Flight Delay Prediction System using Python, SQL, XGBoost, and Streamlit to analyze flight data and predict the probability of flight delays.
# ✈️ Flight Delay Prediction System

An end-to-end **Flight Delay Prediction System** built using Python, SQL, Machine Learning, XGBoost, and Streamlit. The project analyzes historical flight data, performs data exploration and SQL-based analysis, trains machine learning models, and provides an interactive web application for predicting flight delays.

## 📌 Project Overview

Flight delays are a common problem in the aviation industry and can affect passengers, airlines, airport operations, and overall travel efficiency.

This project uses historical flight data to develop a machine learning classification system that predicts whether a flight is likely to be **Delayed** or **Not Delayed**.

The project covers the complete machine learning workflow:

**Data → Cleaning → EDA → SQL Analysis → Feature Engineering → Model Training → Model Evaluation → Threshold Tuning → Streamlit Application**

## 🎯 Objectives

* Analyze historical flight data.
* Clean and prepare the dataset for machine learning.
* Perform exploratory data analysis (EDA).
* Use SQL to analyze flight-delay patterns.
* Identify important factors used by the prediction model.
* Train and compare multiple classification algorithms.
* Handle class imbalance in the target variable.
* Tune the prediction threshold.
* Build an interactive Streamlit application.
* Display flight-delay probability and prediction results.

## 🛠️ Technologies Used

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| Python           | Data processing and machine learning |
| Pandas           | Data manipulation and analysis       |
| NumPy            | Numerical operations                 |
| Scikit-learn     | Machine learning and evaluation      |
| XGBoost          | Final classification model           |
| SQL / SQLite     | Flight data analysis                 |
| Matplotlib       | Data visualization                   |
| Seaborn          | Exploratory data visualization       |
| Streamlit        | Interactive web application          |
| Joblib           | Saving and loading trained models    |
| Jupyter Notebook | Data analysis and experimentation    |

## 📂 Project Structure

```text
flight-delay-prediction/
│
├── app/
│   ├── app.py
│   └── predict.py
│
├── data/
│   ├── cleaned_flights.csv
│   ├── flights_sample.csv
│   ├── flights.db
│   ├── airline_delay_analysis.csv
│   ├── hour_delay_analysis.csv
│   ├── month_delay_analysis.csv
│   └── route_delay_analysis.csv
│
├── models/
│   ├── flight_delay_xgboost.pkl
│   ├── threshold.pkl
│   └── category_mappings.pkl
│
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_sql_analysis.ipynb
│   └── 03_model_training.ipynb
│
├── sql/
│
├── run_app.sh
├── README.md
└── .gitignore
```

## 🔍 Data Cleaning & EDA

The first stage of the project focused on understanding and preparing the flight dataset.

The process included:

* Loading the flight dataset.
* Inspecting the dataset structure.
* Checking missing values.
* Identifying relevant features.
* Cleaning and preparing data for analysis.
* Creating the target variable `DELAYED`.
* Exploring flight-delay patterns.
* Analyzing delays by airline, month, hour, and route.
* Preparing the cleaned dataset for machine learning.

## 🗄️ SQL Analysis

SQLite was used to perform structured analysis of the flight data.

The SQL analysis was used to investigate questions such as:

* Which airlines have more delayed flights?
* How do delays vary by departure hour?
* How do delays vary by month?
* Which routes experience more delays?
* What is the relationship between flight counts and delays?

The SQL results were exported into analysis files for further interpretation and visualization.

## 🤖 Machine Learning

The target variable is:

```text
DELAYED
0 → Not Delayed
1 → Delayed
```

The following classification models were trained and evaluated:

* Logistic Regression
* Random Forest
* XGBoost
* Balanced XGBoost
* Tuned XGBoost

### Class Imbalance

The dataset contains significantly more non-delayed flights than delayed flights.

To address this imbalance, the final XGBoost model used:

```text
scale_pos_weight = 4.4187
```

This gives greater importance to the minority delayed-flight class during model training.

## 🎚️ Threshold Tuning

Instead of relying only on the default probability threshold of 0.50, different thresholds were evaluated.

The tested thresholds ranged from **0.20 to 0.60**.

Based on the tested values, a threshold of **0.55** produced the highest F1-score.

The final application therefore uses:

```text
Decision Threshold = 55%
```

If the predicted delay probability is at least 55%, the application classifies the flight as **Delayed**.

## 📊 Final Model Performance

The final Balanced XGBoost model with the selected 55% prediction threshold produced the following test-set results:

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 71.56% |
| Precision | 33.70% |
| Recall    | 55.96% |
| F1 Score  | 42.07% |
| ROC-AUC   | 71.75% |

These metrics are calculated on the project's test dataset.

## ⭐ Model Feature Importance

The XGBoost model used the following features:

* Departure Hour
* Month
* Airline
* Day
* Day of Week
* Origin Airport
* Distance
* Destination Airport
* Scheduled Time
* Weekend Indicator

The model's feature-importance values indicate which features contributed more strongly to its predictions. They should not be interpreted as proof that a feature directly causes flight delays.

## 🌐 Streamlit Application

The project includes an interactive Streamlit web application.

The user can enter:

* Airline code
* Origin airport
* Destination airport
* Month
* Day
* Day of week
* Departure hour
* Scheduled time
* Flight distance
* Weekend indicator

The application then provides:

* Predicted flight status
* Delay probability
* Risk information
* Decision threshold
* Model performance information

### Example Prediction

Example input:

```text
Airline: DL
Origin: ATL
Destination: JFK
Month: 1
Day: 3
Day of Week: 6
Departure Hour: 10
Scheduled Time: 130 minutes
Distance: 760 miles
Weekend: Yes
```

Example output:

```text
Prediction: DELAYED
Delay Probability: 61.09%
Decision Threshold: 55%
```

## 🔄 Project Workflow

```text
Historical Flight Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
SQL Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Model Training
        ↓
Model Comparison
        ↓
Class Imbalance Handling
        ↓
Threshold Tuning
        ↓
Final XGBoost Model
        ↓
Model Saving
        ↓
Streamlit Application
        ↓
Flight Delay Prediction
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/flight-delay-prediction.git
```

### 2. Open the project

```bash
cd flight-delay-prediction
```

### 3. Install required packages

```bash
pip install pandas numpy scikit-learn xgboost streamlit joblib matplotlib seaborn
```

### 4. Run the Streamlit application

```bash
python3 -m streamlit run app/app.py
```

Alternatively, if `run_app.sh` is executable:

```bash
./run_app.sh
```

The application will open in your browser.

## 📓 Notebooks

The project contains three main notebooks:

### `01_data_cleaning_eda.ipynb`

Contains data cleaning, preparation, and exploratory data analysis.

### `02_sql_analysis.ipynb`

Contains SQLite-based queries and analysis of flight-delay patterns.

### `03_model_training.ipynb`

Contains model training, evaluation, class-imbalance handling, threshold tuning, and model selection.

## 💾 Saved Models

The trained model and supporting files are stored in the `models/` directory.

* `flight_delay_xgboost.pkl` — trained XGBoost model
* `threshold.pkl` — selected prediction threshold
* `category_mappings.pkl` — categorical feature mappings used by the application

## 📸 Application Screenshots

Screenshots of the Streamlit application will be added to this section.

## 🚀 Future Improvements

Possible future improvements include:

* Deploying the Streamlit application online.
* Adding real-time flight information.
* Integrating live weather information.
* Improving categorical encoding for production use.
* Performing additional hyperparameter optimization.
* Adding more advanced model explainability.
* Adding automated model retraining.
* Creating a monitoring dashboard for model performance.

## 💡 Key Learning Outcomes

Through this project, I worked with:

* Real-world data cleaning
* Exploratory data analysis
* SQL data analysis
* Feature engineering
* Classification algorithms
* Imbalanced datasets
* Model evaluation
* Threshold optimization
* XGBoost
* Model serialization
* Streamlit application development
* End-to-end machine learning workflow

## 👨‍💻 Author

**Sankar**

Student Data Science Project

---

⭐ If you find this project useful, feel free to explore the notebooks and application code.
