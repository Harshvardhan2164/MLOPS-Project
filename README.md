# MLOPS Project using MLFLOW

This repository contains two **End-to-End MLOps Pipelines**: one for predicting **Wine Quality** and another for **Student Performance Analysis**. Both projects leverage **MLflow** for experiment tracking and model management.

## 📌 Features

### Wine Quality Prediction
- ✅ **Data Preprocessing** & Feature Engineering  
- ✅ **Model Training & Evaluation** using **ElasticNet Regression**  
- ✅ **MLflow Integration** for tracking metrics & parameters  
- ✅ **CI/CD Pipeline** for automated model deployment  
- ✅ **Web App** for user-friendly wine quality prediction  

### Student Performance Analysis
- ✅ **Data Cleaning & Preprocessing**  
- ✅ **Exploratory Data Analysis (EDA)** for insights  
- ✅ **Model Training & Evaluation** using **Regression Models**
- ✅ **Web App** for predicting student performance  

## 🏰️ Tech Stack

- **Python** (Scikit-Learn, Pandas, NumPy)  
- **MLflow** for tracking & model registry  
- **Flask** for web-based inference  
- **Docker** for containerization  
- **GitHub Actions** for CI/CD  

## Workflows

1. Update config.yaml  
2. Update schema.yaml  
3. Update params.yaml  
4. Update the entity  
5. Update the configuration manager in src config  
6. Update the components  
7. Update the pipeline  
8. Update the main.py  
9. Update the app.py  

### [Dagshub](https://dagshub.com/)

[MLFLOW](https://mlflow.org/docs/latest/index.html)

## 📎 Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/Harshvardhan2164/MLOPS-Project.git
```

2. Select one of the projects
```bash
cd MLOPS-Project/End-to-End\ ML\ Project
```
OR
```bash
cd MLOPS-Project/End-to-End\ Student\ Analysis\ Project
```

2. Create a virtual environment after opening the repository (Use Python Version < 3.11)
```bash
python -m venv env
```

```bash
source env/Scripts/activate
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

4. Run `app.py`
```bash
python app.py
```

5. Open up your localhost and port