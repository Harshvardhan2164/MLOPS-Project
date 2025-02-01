# End-to-End ML Project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update prams.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

## Installation

1. Clone the repository

```bash
git clone https://github.com/Harshvardhan2164/MLOPS-Project.git
```

2. Create a virtual environment after opening the repository (Use Python Version < 3.11)
```bash
python -m venv env
'''
'''bash
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

## ML Flow

[Documentation](https://mlflow.org/docs/latest/index.html)

### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/Harshvardhan2164/MLOPS-Project.mlflow \
MLFLOW_TRACKING_USERNAME = Harshvardhan2164 \
MLFLOW_TRACKING_PASSWORD = cb224190d08b1d4dec2192ba302c4f5bb4173956 \
python script.py

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Harshvardhan2164/MLOPS-Project.mlflow

export MLFLOW_TRACKING_USERNAME=Harshvardhan2164

export MLFLOW_TRACKING_PASSWORD=519f4d6e8f2ce60af489466d4193c4a527af3554
```