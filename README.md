#  Healthcare Analytics System

A full-stack machine learning application designed to predict patient test results (Normal, Abnormal, or Inconclusive) based on various medical and demographic factors. 

##  Features
* **Machine Learning:** Uses a trained model (Logistic Regression) to make real-time predictions.
* **Backend:** Built with FastAPI for high performance and automatic API documentation.
* **Database:** Connected to a PostgreSQL database hosted on Supabase (using SQLAlchemy and connection pooling).
* **Frontend:** A clean, responsive HTML/JS user interface to easily input patient data and view predictions.
* **Automated Training:** Includes a weekly scheduler to retrain the model with fresh data.

##  Tech Stack
* **Python 3** (FastAPI, SQLAlchemy, Scikit-Learn, Pandas)
* **PostgreSQL** (Supabase)
* **HTML / CSS / Vanilla JavaScript**
* **Uvicorn** (ASGI Server)

##  Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/GathirwaNicholus/Gg-healthcare-ml-projectx.git](https://github.com/GathirwaNicholus/Gg-healthcare-ml-projectx.git)
   cd Gg-healthcare-ml-projectx
   ```

2. Set up the virtual environment and install dependencies:

```Bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt # Or install your specific packages
uv add "uvicorn[standard]"
```


3. Environment Variables:
Create a .env file in the root directory and add your Supabase connection string:

```python
DATABASE_URL="postgresql://postgres.[YOUR_PROJECT_ID]:[YOUR_PASSWORD]@[aws-0-eu-central-1.pooler.supabase.com:5432/postgres](https://aws-0-eu-central-1.pooler.supabase.com:5432/postgres)"
```


4. Run the Application:

``` Bash
uv run uvicorn app.main:app --reload --port 8000
Open your browser and navigate to http://127.0.0.1:8000/ to see the UI, or http://127.0.0.1:8000/docs for the interactive API documentation.
```