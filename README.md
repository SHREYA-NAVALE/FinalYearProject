# 🌳 Live Deforestation Monitoring & Permit Verification System

## 🚀 Project Setup Guide

Follow these steps to run the project locally.

---

# 📥 1. Clone Repository

```bash
git clone https://github.com/your-username/FinalYearProject.git
cd FinalYearProject
```

---

# 🧱 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

# 🗄️ 3. Setup PostgreSQL + PostGIS

## Install:

* PostgreSQL 16
* PostGIS 3.4

## Create Database:

```sql
CREATE DATABASE FinalYearProject;
```

## Enable PostGIS:

```sql
CREATE EXTENSION postgis;
```

## Create Tables:

```sql
CREATE TABLE permits (
    permit_id VARCHAR(50) PRIMARY KEY,
    geometry GEOMETRY(POLYGON, 4326),
    issue_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    permit_type VARCHAR(100),
    authority VARCHAR(100),
    project_name VARCHAR(255),
    status VARCHAR(50)
);

CREATE TABLE detected_deforestation (
    detection_id SERIAL PRIMARY KEY,
    geometry GEOMETRY(POLYGON, 4326),
    centroid GEOMETRY(POINT, 4326)
        GENERATED ALWAYS AS (ST_Centroid(geometry)) STORED,
    detected_at DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# ⚙️ 4. Configure Backend DB Connection

Edit:

```bash
backend/db.py
```

Update:

```python
conn = psycopg2.connect(
    dbname="FinalYearProject",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5433"
)
```

---

# ▶️ 5. Run Backend

```bash
cd backend
uvicorn main:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

# 🎨 6. Setup Frontend

```bash
cd frontend

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

# ▶️ 7. Run Frontend

```bash
streamlit run app.py
```

---

# 🧪 8. Test System

1. Open frontend
2. Go to Analytics
3. Click Analyze
4. Check database:

```sql
SELECT * FROM detected_deforestation;
```

---

# 🔥 Features

* Satellite-based deforestation detection
* Permit validation using geospatial data
* PostGIS spatial queries
* Interactive dashboard (Streamlit)

---

# 👥 Team Notes

* Backend → FastAPI
* Frontend → Streamlit
* Database → PostgreSQL + PostGIS

---

# 🚀 Future Work

* Integrate real satellite images
* Add ML-based detection model
* Implement ST_Intersects for illegal detection
