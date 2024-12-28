# PayPredict
The PayPredict is a data-driven web application designed to provide developers with precise salary predictions based on insights from the Stack Overflow Developer Survey 2024. By bridging the gap between raw survey data and meaningful predictions, PayPredict empowers developers to make informed career decisions.

## Introduction
This project is a Machine Learning web application built using Python and Streamlit. The web app predicts salaries based on real-world data. In the first part of the project, we analyze the data and build machine learning models using Linear Regression, Decision trees, and Random Forest regression. We also use GridSearchCV for hyperparameter tuning to optimize the models.
![image](https://github.com/user-attachments/assets/b8eed9d7-a9ea-491d-be91-c50c83c47669)

## Features
- Predicts salaries based on multiple factors.  
- Uses Linear Regression, Decision Tree, and Random Forest Regressor models.  
- Web application built with Streamlit.

## Models used
The data used for this project comes from the Stack Overflow Developer Survey. It contains information about software developers' demographics, education, experience, job roles, and corresponding salaries. We perform data analysis, data preprocessing, and feature engineering to prepare the data for training our machine learning models.

The models used in this project are:

1. Linear Regression: A simple linear model that establishes a relationship between the input features and salaries

2. Decision Tree: A non-linear model that forms a tree-like structure to make decisions based on the input features.

3. Random Forest Regressor: An ensemble model that combines multiple decision trees to improve the accuracy and robustness of predictions.

## Technologies Used  
- Streamlit  
- Python (pandas, scikit-learn, numpy)  
- Stack Overflow Developer Survey 2024 dataset

## Getting Started 
### Installation  
1. Clone the repository: `git clone https://github.com/username/repo-name.git`  
2. Navigate to the project directory: `cd repo-name`  
3. Install dependencies   
4. Run the app: `streamlit run app.py`  

### Usage  
- Open the app in your browser using the provided Streamlit link.  
- Input details such as degree, experience level, and location.  
- View the predicted salary and additional insights.  


