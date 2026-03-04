# Customer-Categorizer 📊 
### End-to-End Machine Learning Deployment with Docker & AWS

This project is a professional-grade Machine Learning application that classifies customers into specific categories based on demographic and behavioral data. It demonstrates a complete MLOps lifecycle, including model training, containerization, and cloud deployment.

---

## 🔗 Live Demo
**Website URL:** [http://3.27.136.81](http://3.27.136.81)  
*(Hosted on an AWS EC2 t3.medium instance)*

---

## 🛠️ Technology Stack
* **Language:** Python
* **Machine Learning:** XGBoost, Scikit-learn
* **Backend Framework:** FastAPI / Uvicorn
* **Database:** MongoDB Atlas (Real-time prediction logging)
* **Cloud Infrastructure:** AWS EC2 (Compute), AWS S3 (Model Artifacts)
* **DevOps:** Docker, Docker Hub

---

## 🏗️ Project Architecture
The application is fully containerized for environment consistency and deployed using a modern cloud-native approach.



1.  **Data Ingestion:** Loads customer data and validates inputs.
2.  **Model Retrieval:** The trained XGBoost model is dynamically pulled from **AWS S3** at startup.
3.  **Containerization:** Packaged into a Docker image (`ankaniitp/customer-categorizer`).
4.  **Cloud Hosting:** Deployed on **AWS EC2** with Port 80 (HTTP) mapped to the internal application port.
5.  **Data Persistence:** Every prediction is logged to a **MongoDB** cluster for future analysis.

---

## 💻 Local Setup
To run this project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/Ankan-Pal/customer-categorizer.git](https://github.com/Ankan-Pal/customer-categorizer.git)
cd customer-categorizer

Create a .env file in the root directory and add your credentials:
MONGO_DB_URL=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1

docker build -t customer-categorizer .
docker run -p 5000:5000 --env-file .env customer-categorizer

# Pull the latest image
docker pull ankaniitp/customer-categorizer:latest

# Run with auto-restart enabled
docker run -d --restart always -p 80:5000 --env-file .env ankaniitp/customer-categorizer:latest


👨‍💻 Author
Ankan Pal Student at IIT Patna, B.Sc. in Computer Science and Data Analytics (CSDA)
Interests: Machine Learning, Cloud Computing, and Data Structures.
LinkedIn: www.linkedin.com/in/
ankan-pal-580755300
Vanity URL name

Email: ankanpal255@gmail.com
