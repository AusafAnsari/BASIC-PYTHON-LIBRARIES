# 📘 Basic Python Libraries – Examples and Usage

This repository provides beginner-friendly Python scripts demonstrating the usage of essential Python libraries: **NumPy**, **Pandas**, and **Seaborn**. These scripts are ideal for students, data science beginners, and developers who want to understand the core functionalities of these powerful tools.

---

## 📂 Files Included

### 🧮 `NUMPY.py`

A basic introduction to **NumPy**, the core library for numerical computing in Python.

#### 🔹 Features:
- Creating and manipulating NumPy arrays
- Array slicing, reshaping, indexing
- Vectorized operations and broadcasting
- Basic mathematical functions and aggregations

**Use Case**: Efficient numerical operations, data preprocessing, and matrix computations.
![image](https://github.com/user-attachments/assets/d6ff1d20-2d6f-4663-a084-822a869daf44)
---

### 📊 `PANDAS.py`

A practical walkthrough of **Pandas**, the go-to library for data manipulation and analysis.

#### 🔹 Features:
- Creating Series and DataFrames
- Reading and writing data (CSV, etc.)
- Data selection, filtering, and sorting
- Handling missing data
- Grouping and aggregation

**Use Case**: Managing tabular data, cleaning datasets, and basic exploratory data analysis.
![image](https://github.com/user-attachments/assets/a6cf78ab-a747-4a1a-aafc-37e062ae8a30)
---

### 📈 `SEABORN.py`

A visual guide to **Seaborn**, a Python visualization library built on top of Matplotlib with beautiful default themes.

#### 🔹 Features:
- Plotting bar charts, line plots, scatter plots
- Visualizing distributions with `distplot`, `boxplot`, `violinplot`
- Relationship plotting with `pairplot`, `heatmap`
- Using built-in datasets for demonstration

**Use Case**: Creating visually appealing statistical graphics to better understand and present data.
![image](https://github.com/user-attachments/assets/bee5548e-9d08-415f-8aa9-13ffa8608ca1)
---
### 🧮 `SKLEARN.py`

This script demonstrates a simple machine learning workflow using **Scikit-learn**. It applies **Linear Regression** to predict students' Math scores based on their English and Science scores.

#### 🔹 Features:
- Generates synthetic student data
- Splits data into training and testing sets
- Trains a Linear Regression model
- Evaluates performance using Mean Squared Error (MSE)
- Prints predicted vs actual Math scores

**Use Case**: Learn how to build, train, and evaluate a basic regression model using Scikit-learn.
![image](https://github.com/user-attachments/assets/0aa46b26-a2e3-4dcd-9618-05b44c704f8d)
---
### 📊 `𝗟𝗜𝗡𝗘𝗔𝗥 𝗥𝗘𝗚𝗚𝗥𝗘𝗦𝗦𝗜𝗢𝗡`

This script combines **NumPy**, **Pandas**, **Matplotlib**, and **Seaborn** to perform basic data generation, analysis, and visualization of student scores.

#### 🔹 Features:
- Generates random scores for Math, English, and Science
- Creates a DataFrame and performs basic statistical analysis
- Plots line graphs of student scores using Matplotlib
- Displays subject-wise score distributions using Seaborn boxplots

**Use Case**: Learn how to generate, analyze, and visualize data using Python's most popular libraries for data science.
![image](https://github.com/user-attachments/assets/8c0f0986-1b87-4c6c-930c-3008858768bf)
![image](https://github.com/user-attachments/assets/34849065-5748-479f-91e6-e8646230ea4b)
---
### 𝗟𝗢𝗚𝗜𝗦𝗧𝗜𝗖 𝗥𝗘𝗚𝗥𝗘𝗦𝗦𝗜𝗢𝗡🎓

This project demonstrates a simple machine learning model to predict student pass/fail status based on their English 🇬🇧 and Science 🔬 scores.

## Overview

The `NP-SK-PD.py` script creates a synthetic dataset 🧪 of student scores, trains a Logistic Regression model 📊, and evaluates its performance. The goal is to predict if a student `Passed` 🎉 (based on a threshold of 75 in Math ➕, which is derived from English and Science scores with some noise).

## Features ✨

* **Data Generation:** Generates synthetic student data 📈 including Math, English, and Science scores.
* **Logistic Regression:** Uses `scikit-learn`'s Logistic Regression for binary classification. ✅
* **Model Evaluation:** Provides accuracy and a detailed classification report. 🎯
* **Train-Test Split:** Splits data for robust model evaluation. ✂️
  ![image](https://github.com/user-attachments/assets/29f25d3c-b9fa-4b80-ac70-efb0fd7784c7)
  
---
### 🔍 `CONFUSION_MATRIX.py`

This script demonstrates the use of **DecisionTreeClassifier** from Scikit-learn and how to compute a **confusion matrix** for evaluating a simple classification model.

#### 🔹 Features:
- Trains a Decision Tree on a small height-weight dataset
- Classifies data into "Short" or "Tall" categories
- Evaluates the model using a confusion matrix

**Use Case**: Understand how classification results are assessed using confusion matrices in supervised learning.
![image](https://github.com/user-attachments/assets/6c4dbb62-3d9b-4b96-b44d-b95b5382abdf)

---
### 🌲 `RANDOM-FOREST.py`

This script compares the performance of a **Decision Tree Classifier** and a **Random Forest Classifier** using a synthetic dataset of student scores.

#### 🔹 Features:
- Generates a dataset of 200 students with scores in Math, English, and Science
- Creates a binary target variable for passing or failing based on Math scores
- Trains and evaluates both Decision Tree and Random Forest classifiers
- Displays accuracy and classification reports for both models

**Use Case**: Understand the difference in performance between single decision trees and ensemble methods like Random Forest in binary classification tasks.
![image](https://github.com/user-attachments/assets/6ded29ea-c44a-4172-89e5-9c29bb24756b)

---
## 🧰 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AusafAnsari/BASIC-PYTHON-LIBRARIES.git
   ```

2. **Navigate to the folder:**
   ```bash
   cd BASIC-PYTHON-LIBRARIES
   ```

3. **Run any script:**
   ```bash
   python NUMPY.py
   python PANDAS.py
   python SEABORN.py
   ```

---

## 📦 Requirements

Install the required libraries using:
```bash
pip install numpy pandas seaborn matplotlib
```

---

## 👨‍💻 Author

**Ausaf Ansari**  
Intern at DoxPro Robotics | AI/ML Enthusiast | Exploring Python for Data Science

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---



--


