#  Student Performance Prediction using Linear Regression

A Machine Learning project that predicts student performance based on academic and lifestyle-related factors using **Linear Regression**. The project includes model training, performance evaluation, and a user-friendly **Streamlit web application** for making predictions.

##  Project Overview

Understanding the factors that influence student performance can help identify patterns in academic outcomes. This project uses a supervised Machine Learning approach to learn the relationship between student-related features and a numerical performance index.

The trained model can be used to generate predictions from input values supplied through an interactive web interface.

##  Objectives

- Build a predictive model using Linear Regression.
- Explore and prepare the dataset for Machine Learning.
- Evaluate the model using appropriate regression metrics.
- Develop an interactive Streamlit application.
- Understand the end-to-end workflow of a Machine Learning project.

##  Dataset

The project uses student performance data containing numerical and categorical features.

The features used during model training include:

| Feature | Description |
|---|---|
| Hours Studied | Number of hours spent studying |
| Previous Scores | Student's previous academic scores |
| Extracurricular Activities | Whether the student participates in extracurricular activities |
| Sleep Hours | Average hours of sleep |
| Sample Papers Practiced | Number of practice papers completed |

**Target variable:** Performance Index

##  Technologies Used

- **Python** — programming language
- **Pandas & NumPy** — data handling and numerical operations
- **Scikit-learn** — model training and evaluation
- **Matplotlib / Seaborn** — data visualization, if used in the notebooks
- **Streamlit** — interactive web application
- **Pickle** — saving and loading the trained model

##  Project Workflow

1. **Data Loading:** Load the dataset and inspect its structure.
2. **Data Cleaning:** Check data quality and handle duplicate or invalid records where necessary.
3. **Exploratory Data Analysis:** Explore feature distributions and relationships.
4. **Feature Selection:** Separate the input features from the target variable.
5. **Train-Test Split:** Split the data into training and testing sets.
6. **Model Training:** Train a Linear Regression model using the training data.
7. **Model Evaluation:** Evaluate predictions on unseen test data.
8. **Model Persistence:** Save the trained model for reuse.
9. **Web Application:** Build a Streamlit interface for user input and prediction.

##  Machine Learning Model

This project uses **Linear Regression**, a supervised learning algorithm that models the relationship between input features and a continuous numerical target.

The model learns coefficients for the input features during training and uses them to estimate the target value for new observations.

##  Model Evaluation

The model was evaluated using the following regression metrics:

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 1.60 |
| Mean Squared Error (MSE) | 4.13 |
| Root Mean Squared Error (RMSE) | 2.03 |
| R² Score | 0.99 |

These are the previously recorded evaluation results for this project. The MAE and RMSE describe prediction error, while the R² score indicates how much of the target's variation is explained by the model on the evaluated data.

##  Streamlit Web Application

The project includes a Streamlit application that allows users to enter student-related information and receive a model prediction through a simple interface.

The application loads the saved model rather than training it again every time a prediction is requested.

##  Project Structure

```text
student-performance-prediction/
│
├── app.py
├── linear.pkl
├── student.ipynb
├── Student_Performance.csv
├── requirements.txt
└── README.md
```

*Note: Adjust the filenames above to match the files actually present in your repository.*

##  Getting Started

### 1. Clone the repository

```bash
git clone <https://github.com/Priyanka200702/Student-performance-prediction.git>
cd student-performance-prediction
```

### 2. Install dependencies

It is recommended to create and activate a virtual environment before installing the required packages.

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

##  Key Learnings

Through this project, I practised:

- The fundamental workflow of supervised Machine Learning.
- Preparing data for model training.
- Training and evaluating a regression model.
- Understanding regression evaluation metrics.
- Saving and reusing a trained model.
- Building a simple interactive application with Streamlit.


---

*This project was developed as part of my journey in learning Machine Learning and building practical projects.*
