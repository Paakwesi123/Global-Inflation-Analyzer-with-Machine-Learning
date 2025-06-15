

#  Global Inflation Analyzer

**Global Inflation Analyzer** is a data science project that explores historical inflation rates across various countries from **1980 to 2024**, with a focus on **predicting future inflation trends**. The project performs comprehensive **data cleaning**, **exploratory data analysis (EDA)**, and **machine learning** to forecast inflation rates — particularly using **Ghana** as a case study for future predictions (2025–2029).


##  Table of Contents

* [Project Objectives](#project-objectives)
* [Dataset](#dataset)
* [Technologies Used](#technologies-used)
* [How It Works](#how-it-works)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Machine Learning Model](#machine-learning-model)
* [Outputs](#outputs)
* [How to Run the Project](#how-to-run-the-project)
* [Future Improvements](#future-improvements)


##  Project Objectives

* Clean and transform a global inflation dataset covering over 40 years
* Visualize inflation trends for selected countries (e.g., USA, Ghana, Japan, Germany, Argentina)
* Train a machine learning model to predict future inflation
* Focus on **Ghana's** inflation from 2025 to 2029
* Save visualizations and predictions in accessible formats


##  Dataset

* **File**: `global_inflation_data.csv`
* **Source**: Public dataset
* **Size**: Covers over 190 countries from 1980 to 2024
* **Columns**:

  * `country_name`: Name of the country
  * `1980–2024`: Columns representing inflation rates for each year


##  Technologies Used

* **Python 3**
* **Pandas** – Data manipulation
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning
* **VS Coder** – Development environment


##  How It Works

1. **Load and Melt the Data**:
   The inflation data (wide format) is melted into a long format with three columns: `country_name`, `year`, and `inflation`.

2. **Clean the Data**:
   All missing inflation values are dropped. The `year` column is converted to integer for analysis.

3. **EDA & Visualization**:
   Trends for selected countries are plotted over time to show how inflation has evolved.

4. **Model Training**:

   * Focus is placed on **Ghana's** data.
   * A **linear regression** model is trained on the years vs. inflation rates.
   * The model is evaluated using RMSE (Root Mean Squared Error).

5. **Prediction**:
   The model predicts inflation rates for **2025–2029**, and results are saved in a `.csv` file.


##  Exploratory Data Analysis

Inflation trend plots are generated for the following countries:

* United States 🇺🇸
* Ghana 🇬🇭
* Japan 🇯🇵
* Germany 🇩🇪
* Argentina 🇦🇷

These plots show how different economies have evolved in inflation control or instability over the years.


##  Machine Learning Model

* **Algorithm**: Linear Regression
* **Train/Test Split**: 80/20
* **Target Country**: Ghana
* **Performance Metric**: RMSE
* **Prediction Horizon**: 2025 to 2029


##  Outputs

1. **Visualization**:

   * `inflation_trends.png`: A line graph showing historical inflation trends for selected countries.

2. **CSV Output**:

   * `ghana_inflation_predictions.csv`: A CSV file containing predicted inflation rates for Ghana from 2025–2029.


## ▶ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Paakwesi123/Global-Inflation-Analyzer.git
cd Global-Inflation-Analyzer
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Script

```bash
python main.py
```

Output files (`.png`, `.csv`) will be saved in the project directory.


##  Future Improvements

* Predict for more countries (multivariate modeling)
* Use advanced models like LSTM, XGBoost, or ARIMA
* Build a dashboard with **Streamlit** or **Power BI**
* Add API integration to fetch real-time inflation data
* Host as a web app for user interaction




