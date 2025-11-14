# 🌲 Forest Fire Weather Index (FWI) Prediction Using Machine Learning

## 🔥 Project Overview
This project predicts the **Forest Fire Weather Index (FWI)** using a machine learning model trained on the Algerian Forest Fire Dataset.  
The app is deployed using **Flask + Render**, and provides a clean web interface for real-time fire index prediction.

---

## 🚀 Live Demo
🔗 **Hosted URL:**  
https://testforestfires-1-ktm1.onrender.com/

---

## 🧠 Tech Stack

### Machine Learning
- Python  
- NumPy  
- Pandas  
- Scikit-Learn  
- Ridge Regression  
- StandardScaler  

### Backend
- Flask  
- Gunicorn  

### Frontend
- HTML  
- CSS  

### Deployment
- Render  
- GitHub  

---

## 📊 Dataset
The model uses the **Algerian Forest Fire Dataset**, which contains fire-related and meteorological features from:

- **Bejaia Region**
- **Sidi Bel-Abbes Region**

### Features used for prediction:

Temperature
RH
Ws
Rain
FFMC
DMC
ISI
Classes
Region


---

## 🧪 Model Training Pipeline

1. Data Cleaning  
2. Feature Scaling using StandardScaler  
3. Ridge Regression Model Training  
4. Model Serialization using pickle  
5. Backend prediction using Flask  

Saved files:

models/
├── ridge.pkl
└── scaler.pkl


---

## 🖥️ Web Interface

The app includes a user-friendly web form with **9 input fields**:

- Temperature (°C)  
- Relative Humidity (RH %)  
- Wind Speed (km/h)  
- Rain (mm)  
- FFMC  
- DMC  
- ISI  
- Classes (0 = No Fire, 1 = Fire)  
- Region (0 = Bejaia, 1 = Sidi Bel-Abbes)

After submission, the app displays the **FWI prediction** clearly in a result card.

---

## 📂 Project Structure

Project Folder
│── app.py
│── requirements.txt
│── Procfile
│
├── models/
│ ├── ridge.pkl
│ └── scaler.pkl
│
├── templates/
└── home.html


### Clone the repository
git clone <https://github.com/rajanSoni0/testforestfires>


## ⭐ Future Enhancements
- Loading animations  
- Better error handling  
- Logging user predictions  
- More ML models (Random Forest, XGBoost)  
- Dashboard with graphs  
- Custom domain + HTTPS  

---

## 🤝 Contributing
Contributions are welcome!

---

## 💡 Author
**Rajan Soni**  
CSE Engineering Student  
Machine Learning & Backend Developer
