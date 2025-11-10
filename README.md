# 🚗 Vehicle Data Intelligence System — MLOps Project

An end-to-end **Machine Learning Operations (MLOps)** project that automates the entire lifecycle — from **data ingestion** to **deployment** — using **AWS Cloud Services**, **Docker**, **MongoDB**, and **GitHub Actions (CI/CD)**.
This project demonstrates how modern ML applications are built, trained, validated, containerized, and deployed seamlessly in production.

---

## 🧠 Project Overview

This project is designed to **predict and analyze vehicle data** using a scalable and modular architecture.
It follows an enterprise-level **MLOps architecture** — ensuring automation, reliability, versioning, and scalability.

**Key Highlights:**

* 📦 Modular Python package structure using `setup.py` and `pyproject.toml`
* ☁️ Data hosted on **MongoDB Atlas**
* 🪵 Centralized **Logging** and custom **Exception Handling**
* ⚙️ ML Pipeline with modular **Data Ingestion**, **Validation**, **Transformation**, **Training**, and **Evaluation**
* 🚀 Automated deployment via **Docker**, **GitHub Actions**, and **AWS EC2**
* 🧰 Model & artifact management via **AWS S3**
* 🔁 Continuous Integration and Continuous Deployment (CI/CD)
* 📈 Interactive EDA & Feature Engineering notebooks
* 🧩 Fully reproducible environment using **Conda**

---

## 🏗️ Project Setup

### 1️⃣ Project Template Initialization

```bash
python template.py
```

This script auto-generates the project folder structure.

---

### 2️⃣ Package Setup

Define package metadata and dependencies using:

* `setup.py`
* `pyproject.toml`


---

### 3️⃣ Virtual Environment Setup

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # verify installed packages
```

---

## 🗄️ MongoDB Atlas Setup

1. Sign up at [MongoDB Atlas](https://www.mongodb.com/atlas/database)
2. Create a new project and cluster (M0 tier - free)
3. Create a DB user with username/password
4. Add IP Access: `0.0.0.0/0`
5. Get the **Connection String** for Python (save it securely)
6. Create a `notebook/` folder and use Jupyter Notebook to push data into MongoDB
7. Verify data in MongoDB → *Browse Collections*

---

## 🧾 Logging, Exception Handling & Notebooks

* Implemented **custom logger** and **exception classes**
* Integrated with demo scripts for validation
* Includes EDA and Feature Engineering notebooks

---

## 🧩 Data Pipeline Components

### 🧠 Data Ingestion

* Reads data from MongoDB
* Transforms JSON → Pandas DataFrame
* Stores metadata as artifacts

**Key Files:**

* `constants/__init__.py`
* `configuration/mongo_db_connections.py`
* `data_access/proj1_data.py`
* `entity/config_entity.py`
* `entity/artifact_entity.py`
* `components/data_ingestion.py`

Set MongoDB connection URL in environment:

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster-url"
```

---

### ✅ Data Validation

Defines schema in `config/schema.yaml`
Validates structure, datatypes, and missing values.

---

### 🔄 Data Transformation

Applies preprocessing pipelines and feature transformations.
Stores transformers and encoders as serialized objects.

---

### 🧮 Model Trainer

Trains ML model using transformed data and saves the model artifact.

---

## ☁️ AWS Integration

### AWS Services Used

* **IAM** → User roles & credentials
* **S3** → Model & artifact storage
* **EC2** → Deployment
* **ECR** → Docker image registry

Set AWS credentials:

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

**Key Constants**

```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```

---

## 🧱 Model Evaluation & Pusher

* Evaluates new model performance
* Pushes approved models to AWS S3 for versioning

---

## 🔮 Prediction Pipeline & Web App

* Flask-based API (`app.py`)
* Routes:

  * `/` → Home
  * `/predict` → Run predictions
  * `/training` → Trigger model training

Add static assets in:

```
static/
templates/
```

---

## 🐳 Dockerization & CI/CD

### Docker Setup

* `Dockerfile`
* `.dockerignore`

### GitHub Actions Workflow

* Located in `.github/workflows/aws.yaml`
* Automates:

  * CI (Build & Test)
  * CD (Push Docker image → ECR → Deploy on EC2)

---

## 🧰 AWS Deployment Workflow

1. Create **IAM user** (`usvisa-user`) for GitHub Actions

2. Create **ECR repository**

   ```
   vehicleproj
   ```

3. Launch **EC2 instance**:

   * Ubuntu Server 24.04 (t2.medium)
   * Port: `5080`
   * Add Security Group rules for inbound traffic

4. Install Docker on EC2:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

5. Configure **Self-Hosted Runner** for GitHub Actions:

   * Settings → Actions → Runners → New self-hosted runner
   * Follow terminal commands on EC2

6. Add GitHub Repository Secrets:

   * `AWS_ACCESS_KEY_ID`
   * `AWS_SECRET_ACCESS_KEY`
   * `AWS_DEFAULT_REGION`
   * `ECR_REPO`

7. Commit & push — GitHub Actions will automatically deploy to EC2.

---

## 🌐 Accessing the Application

Once deployed, open your app in browser:

```
http://<EC2-Public-IP>:5080
```

---

## 🧾 Project Architecture

```
📦 vehicle-mlops
├── src/
│   ├── components/
│   ├── configuration/
│   ├── data_access/
│   ├── entity/
│   ├── pipeline/
│   └── aws_storage/
├── notebook/
├── templates/
├── static/
├── setup.py
├── pyproject.toml
├── requirements.txt
├── app.py
├── Dockerfile
└── .github/workflows/aws.yaml
```

---

## 🧠 Tech Stack

| Category                   | Tools/Tech                              |
| -------------------------- | --------------------------------------- |
| **Language**               | Python 3.10                             |
| **Data Storage**           | MongoDB Atlas                           |
| **ML/EDA**                 | Pandas, NumPy, Scikit-learn, Matplotlib |
| **Pipeline Management**    | Custom Modular Architecture             |
| **Cloud Platform**         | AWS (EC2, S3, ECR, IAM)                 |
| **Orchestration**          | GitHub Actions (CI/CD)                  |
| **Containerization**       | Docker                                  |
| **Environment Management** | Conda                                   |
| **Web Framework**          | Flask                                   |

---

## 🏁 Final Output

✅ Fully automated ML pipeline
✅ Model deployed on AWS EC2
✅ Continuous delivery with GitHub Actions
✅ Production-grade modular codebase

---

<!-- ### 🌟 Author

**Armaan Haider**
<!-- *MLOps Enthusiast | Data Scientist | Cloud Developer*

📧 Reach me on [LinkedIn](#) or [GitHub](#)

---

Would you like me to **add emojis, color highlights (for GitHub Markdown), and badges** (like “Built with Python”, “AWS Certified”, “CI/CD Enabled”, etc.) to make it even more visually appealing for recruiters? --> -->
