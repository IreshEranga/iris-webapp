
# 🌸 Iris Flower Species Prediction Web App

A beginner-friendly Machine Learning web application that predicts the species of an Iris flower based on its petal and sepal dimensions.

## 🚀 Project Overview

This project uses the famous [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) and a machine learning model (Random Forest) to classify flowers into:
- **Setosa**
- **Versicolor**
- **Virginica**

Users can input measurements of a flower via a simple web form, and the app will predict its species in real time.

---

## 📁 Folder Structure

```
iris-webapp/
├── model/
│   └── iris_model.pkl          # Trained ML model
├── templates/
│   └── index.html              # Frontend HTML
├── static/
│   └── style.css               # Custom styles (optional)
├── app.py                      # Flask web application
├── train_model.py              # Script to train the ML model
├
└── README.md                   
```

---

## 🧠 Tech Stack

- **Python 3**
- **Flask** - Web framework
- **Scikit-learn** - For training the ML model
- **Bootstrap** - For responsive frontend design

---

## ⚙️ How to Run Locally

### 1. Clone this Repository
```bash
git clone https://github.com/IreshEranga/iris-webapp.git
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate
```

### 3. Install Requirements
```bash
python -m pip install
```

### 4. Train the Model
```bash
python train_model.py
```

### 5. Run the Web App
```bash
python app.py
```
Then go to `http://127.0.0.1:5000` in your browser.

---

## 📷 Screenshots
![image](https://github.com/user-attachments/assets/e33f97b8-0a67-43ca-8b37-fa3307ceb437)

---

## 📝 Features

- 🌼 Real-time Iris flower prediction
- 🎯 Simple and intuitive UI
- 🔬 Pre-trained ML model using scikit-learn
- 📦 Flask backend with HTML/CSS frontend

---

## 📚 Learnings

This project helps you learn:
- How to load and train ML models
- Flask app structure and routing
- Frontend-backend integration
- Using `pickle` to serialize and load models

---

## 🌐 Deployment (Optional)

Deploy easily with services like:
- **Render.com**
- **PythonAnywhere**
- **Heroku (deprecated free tier)**

---

## 🤝 Contributing

Feel free to fork this project, suggest improvements, or add new features. Contributions are welcome!

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---
