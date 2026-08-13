# User-Defined Linear Regression Model

A **menu-driven Machine Learning project** built using Python that allows users to perform Linear Regression on their own CSV datasets.

The project supports both **Simple Linear Regression** and **Multiple Linear Regression** and provides data preprocessing, prediction, visualization, and model evaluation features.

## 🚀 Features

- Load any CSV dataset
- Display the first 5 rows
- Check missing values
- Remove rows containing missing values
- Select dependent and independent variables dynamically
- Automatically perform 80:20 train-test split
- Train a Linear Regression model
- Make predictions on test data
- Make specific predictions using user-provided values
- Visualize Simple Linear Regression
- Visualize Multiple Linear Regression
- Calculate:
  - MSE
  - RMSE
  - R² Score
- Interactive command-line menu
- Basic input validation and error handling

## 🧠 Machine Learning Workflow

```text
CSV Dataset
     ↓
Data Loading
     ↓
Data Inspection
     ↓
Missing Value Check
     ↓
Data Cleaning
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Linear Regression
     ↓
Prediction
     ↓
Visualization
     ↓
Model Evaluation
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/user-defined-linear-regression.git
```

Move into the project directory:

```bash
cd user-defined-linear-regression
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python program:

```bash
python linear_regression.py
```

You will see the main menu:

```text
==============================================
   USER-DEFINED LINEAR REGRESSION MODEL
==============================================
Made by Shivam Singh Jani
----------------------------------------------
1. Load Dataset
2. Show Dataset
3. Check Missing Values
4. Remove Missing Values
5. Select Variables & Train Model
6. Exit
----------------------------------------------
```

### Example

Suppose your dataset contains:

```text
Experience
Salary
Age
```

You can select:

```text
Dependent variable: Salary
Independent variable: Experience
```

The program will train a Linear Regression model and allow you to predict salary based on experience.

For Multiple Linear Regression, you can select:

```text
Independent variables:
Experience, Age
```

## 📊 Model Evaluation

The project uses three evaluation metrics.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

```text
MSE = Σ(y - ŷ)² / n
```

Lower MSE generally indicates better predictions.

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

```text
RMSE = √MSE
```

It is expressed in the same units as the target variable.

### R² Score

R² measures how much of the variation in the dependent variable is explained by the regression model.

A value closer to **1** generally indicates a better fit.

## 📈 Visualization

### Simple Linear Regression

The program displays:

- Actual data points
- Regression line

### Multiple Linear Regression

The program displays:

- Actual vs Predicted values
- Perfect prediction reference line

## 📁 Project Structure

```text
user-defined-linear-regression/
│
├── linear_regression.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 📋 Requirements

Python 3.9 or newer is recommended.

Required libraries:

```text
pandas
numpy
matplotlib
scikit-learn
```

## 🔮 Future Improvements

Possible future improvements include:

- Add Logistic Regression
- Add Polynomial Regression
- Add feature scaling
- Add automatic categorical-variable encoding
- Add outlier detection
- Add correlation analysis
- Add automatic model selection
- Add model saving using Joblib
- Add a graphical user interface
- Add Streamlit web interface
- Add automatic PDF model reports

## 👨‍💻 Author

**Shivam Singh Jani**

B.Tech Computer Science Engineering  
AI/ML Enthusiast | Python | SQL | Machine Learning

## ⭐ Project Goal

This project was created to understand the complete Machine Learning workflow, from **loading and cleaning data to training, prediction, visualization, and evaluation**.

If you find this project useful, consider giving the repository a ⭐.