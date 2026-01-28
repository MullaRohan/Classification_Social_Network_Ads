# Customer Buy Prediction

A simple web application that predicts whether a customer is likely to buy a product based on their **Age**, **Salary**, and **Gender** using a machine learning model.

---

## 🗂 Dataset
The dataset used for training the model can be found [here](https://www.kaggle.com/datasets/rakeshrau/social-network-ads).

**Input Features:**
- Age
- Salary
- Gender

**Output:**
- Prediction: `Buy` or `Not Buy`

---

## ⚡ Features
- Interactive web form to input customer data.
- FastAPI backend serving the prediction model.
- Real-time prediction results displayed on the frontend.
- Input validation for Age, Salary, and Gender.

---

## 🚀 Setup & Installation

### 1️⃣ Create a virtual environment
```bash
python -m venv .venv
```
### 2️⃣ Activate the virtual environment
```bash
#on windows
.venv\Scripts\activate
#on Mac
source env/bin/activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the FastAPI application
```bash
uvicorn app:app --reload
```
- Open your browser and go to `http://127.0.0.1:8000` to access the web interface.
---
🖥 Usage

1. Enter Age (18-60)  
2. Enter Salary (e.g., 15,000 - 150,000)  
3. Select Gender  
4. Click Predict to see if the customer is likely to buy.  
---
📌 Author

Rohan Mulla  
Dept of CSE  
Rabindra Maitree University, Kushtia  
For more details, feel free to contact me.  
mdrohanislam444@gmail.com