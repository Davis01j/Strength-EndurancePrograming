File Structure: This file structure is optimized for development in Jupyter Notebooks. 
                Methodology is to use Jupyter Notebook for quick dev and transition to 
                application scripts quickly. 


    running-plan-project/
    ├── env/      ← project virtual environment
    ├── airflow-env/      ← airflow virtual environment
    ├── notebooks/
    │   └── devnotebook.ipynb       ← your exploratory analyses
    ├── src/
    │   ├── consolidate.py        ← pure-Python functions
    ├── tests/
    │   └── test_plan_generator.py  ← Python scripts in testing
    ├── data/
    │   └── sqlite.db
    │   └── plans/
    │       └── endurance/  
    │       └── strength/  
    │   └── rawdata/
    │       └── bronze/  
    │          └── whoop/  
    │          └── garmin/  
    │          └── consolidated/  
    │       └── silver/ 
    │       └── gold/   
    ├── requirements.txt
    └── README.md


ENVIRONMENT SETUP:

1. Create a Python Virtual Environment for the project
2. Create a Python Virutual Environment for Airflow


SCRIPTS:

1. consolidate.py #Crawls source folder for all CSV & JSON files. Creates a copy in destination folder. Updates names if duplicates. 
    python3 consolidate.py /PATH/TO/SOURCE/FOLDER /PATH/TO/DESINATION/FOLDER

2. 