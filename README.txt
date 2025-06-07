File Structure: This file structure is optimized for development in Jupyter Notebooks. 
                Methodology is to use Jupyter Notebook for quick dev and transition to 
                application scripts quickly. 


    running-plan-project/
    ├── notebooks/
    │   └── prototype.ipynb       ← your exploratory analyses
    ├── src/
    │   ├── __init__.py
    │   └── plan_generator.py     ← pure-Python functions
    ├── tests/
    │   └── test_plan_generator.py
    ├── data/
    │   └── sqlite.db
    │   └── rawdata/
    │       └── bronze/  
    │       └── silver/ 
    │       └── gold/   
    ├── requirements.txt
    └── README.md
