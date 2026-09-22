# DATA SCIENCE RESEARCH CAPSTONE

## Predicting Student Academic Performance Using Machine Learning

### Research Report / Whitepaper

---

## Abstract

Student academic performance is influenced by several measurable factors such as study time, attendance, previous academic achievement, assignment completion, and sleep habits.

This project presents a data science workflow for predicting a student's final academic score using these factors. The project includes data collection, data cleaning, exploratory data analysis, feature selection, machine learning model training, prediction, and model evaluation.

A Random Forest Regression model is used as the primary predictive model. The project demonstrates how machine learning can be used for educational data analysis and can provide a foundation for academic monitoring and early-support systems.

---

## 1. Introduction

Educational institutions generate large amounts of student-related data. When this data is analyzed properly, it can provide useful information about academic performance.

Traditional academic evaluation mainly focuses on examination results. Data science can combine several factors such as attendance, study hours, previous scores, assignment completion, and sleep habits.

The purpose of this project is to develop a machine learning workflow that predicts student final scores using selected academic and study-related factors.

---

## 2. Research Question

Can student academic performance be predicted using study habits, attendance, previous academic performance, assignment completion, and sleep hours?

---

## 3. Objectives

The main objectives of this project are:

1. To analyze student academic data.
2. To clean and preprocess the dataset.
3. To perform exploratory data analysis.
4. To identify important performance-related features.
5. To train a machine learning regression model.
6. To evaluate the model using standard performance metrics.
7. To generate predicted academic scores.
8. To discuss practical applications of the results.

---

## 4. Literature Background

Educational data mining and learning analytics use student-related information to understand learning outcomes.

Predictive modelling can help educational institutions identify patterns in student performance. Information such as previous academic results, attendance, and student activity can be used as predictive features.

However, predictive systems depend on data quality and should be used as decision-support tools rather than replacing teachers or academic judgment.

---

## 5. Dataset

The dataset contains 100 student records and six variables.

### Variables

| Variable | Description |
|---|---|
| study_hours | Approximate study hours |
| attendance | Attendance percentage |
| previous_score | Previous academic score |
| assignments_completed | Number of completed assignments |
| sleep_hours | Average sleep hours |
| final_score | Final academic score |

The target variable is `final_score`.

The remaining five variables are used as input features.

---

## 6. Data Preprocessing

The dataset is loaded using the Pandas library.

The following preprocessing steps are performed:

- Dataset loading
- Duplicate record removal
- Missing value checking
- Missing record removal
- Feature and target separation
- Train-test splitting
- Feature scaling

The dataset is divided into 80% training data and 20% testing data.

StandardScaler is used to scale the numerical features before model training.

---

## 7. Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the dataset and relationships between variables.

The project uses:

- Descriptive statistics
- Correlation analysis
- Correlation heatmap
- Feature importance visualization
- Actual versus predicted score comparison

The correlation analysis helps identify relationships between academic factors and final scores.

---

## 8. Machine Learning Methodology

Random Forest Regression is selected as the main machine learning model.

Random Forest Regression combines multiple decision trees and uses their predictions to generate a final prediction.

The model is trained using:

- Study hours
- Attendance
- Previous score
- Assignments completed
- Sleep hours

The trained model predicts the final academic score.

---

## 9. Model Evaluation

The model is evaluated using the following metrics:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted scores.

### Mean Squared Error (MSE)

MSE measures the average squared prediction error.

### Root Mean Squared Error (RMSE)

RMSE represents prediction error in the same unit as the target variable.

### R² Score

R² measures how much variation in the target variable is explained by the model.

The exact metric values are generated when the Python program is executed.

---

## 10. Results and Discussion

The project generates an actual-versus-predicted score table.

The Random Forest model also generates feature importance values. These values help identify which input variables contribute most to the model's predictions.

The results should be interpreted according to the available dataset.

Since the dataset contains 100 records and is designed for a capstone demonstration, the results should not be generalized to all students without testing the model on larger real-world datasets.

---

## 11. Practical Applications

A similar machine learning system can be used in educational environments for:

- Academic performance monitoring
- Student progress dashboards
- Early academic support
- Identification of students requiring additional attention
- Academic planning
- Data-driven educational analysis

The prediction should be used together with teacher observations and student feedback.

---

## 12. Limitations

The project has some limitations:

1. The dataset is relatively small.
2. Only a limited number of factors are included.
3. Real academic performance may depend on many additional factors.
4. The dataset is designed for demonstration purposes.
5. Results require validation on larger real-world datasets.

Future work can include larger datasets, additional features, cross-validation, hyperparameter tuning, and comparison of multiple machine learning algorithms.

---

## 13. Conclusion

This project demonstrates an end-to-end data science workflow for predicting student academic performance.

The workflow includes data preprocessing, exploratory analysis, feature selection, machine learning model training, prediction, and evaluation.

The project shows how educational data can be transformed into useful analytical insights.

Machine learning predictions can support academic monitoring and planning, but they should be treated as supporting information rather than definitive judgments about individual students.

---

## 14. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Sc
