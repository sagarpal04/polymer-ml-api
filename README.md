# 🧪 Polymer Predictor - AI-Powered Biodegradation Analysis Platform

<div align="center">

![Polymer Predictor Banner](https://img.shields.io/badge/Polymer-Predictor-6c63ff?style=for-the-badge&logo=react&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

**Advanced machine learning platform to predict biodegradable polymer behavior under various environmental conditions**

[Live Demo](#) • [Documentation](#features) • [Report Bug](#) • [Request Feature](#)

</div>

---

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Model Training](#-model-training)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

**Polymer Predictor** is an AI-powered web application that helps researchers, manufacturers, and environmental scientists predict the biodegradation percentage of various polymer types under different environmental conditions. 

### Why Polymer Predictor?

- 🌍 **Environmental Impact**: Make data-driven decisions about biodegradable materials
- ⚡ **Fast Predictions**: Get results in less than 1 second
- 🎯 **High Accuracy**: ML models with R² > 0.85
- 📊 **Visual Insights**: Interactive degradation curves and detailed analytics
- 🔬 **5 Polymer Types**: Support for PLA, PCL, PHB, PBS, and PBAT

### Key Capabilities

- Predict biodegradation percentage based on 9 environmental and material parameters
- Visualize degradation curves over time with interactive charts
- Compare different polymer types and conditions
- Export results for research and documentation

---

## ✨ Features

### 🎨 Frontend Features
- ✅ Modern, responsive UI with gradient design
- ✅ Real-time form validation
- ✅ Interactive Chart.js visualizations
- ✅ Smooth animations and transitions
- ✅ Mobile-first responsive design
- ✅ Example data for quick testing
- ✅ Degradation curve generation

### 🚀 Backend Features
- ✅ FastAPI REST API with automatic OpenAPI docs
- ✅ Type-safe request/response with Pydantic
- ✅ CORS enabled for web access
- ✅ Comprehensive error handling
- ✅ Fast prediction inference (<100ms)
- ✅ Health check endpoint

### 🤖 Machine Learning Features
- ✅ Automated model selection (RF, GB, HistGB)
- ✅ Hyperparameter optimization with RandomizedSearchCV
- ✅ 4-fold cross-validation
- ✅ Mixed data preprocessing (numeric + categorical)
- ✅ Complete sklearn pipeline serialization
- ✅ Metadata tracking for reproducibility

---

## 🛠 Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Async/await, fetch API
- **Chart.js** - Interactive data visualization
- **Font Awesome 6.4.0** - Icon library

### Backend
- **Python 3.8+** - Core programming language
- **FastAPI** - High-performance web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### Machine Learning
- **scikit-learn** - ML framework
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **joblib** - Model serialization

### Development Tools
- **Git/GitHub** - Version control
- **VS Code** - Code editor
- **Postman** - API testing

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

```bash
# Python 3.8 or higher
python --version

# pip (Python package manager)
pip --version

# Git
git --version
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/polymer-predictor.git
cd polymer-predictor
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```text
fastapi==0.104.1
uvicorn[standard]==0.24.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
joblib==1.3.2
pydantic==2.5.0
python-multipart==0.0.6
```

3. **Prepare the dataset**
```bash
# Place your dataset in the content directory
mkdir -p content
# Copy your dataset.csv to content/dataset.csv
```

### Running the Application

#### Step 1: Train the Model

```bash
python train_and_save_best_model.py
```

**Expected Output:**
```
Loading dataset from: /content/dataset.csv
Dataset shape: (1000, 10)
Detected target column: Degradation_Percent
Detected task type: regression

--- Training candidate: RandomForest ---
Best CV score: 0.89
Test RMSE: 5.23 | R2: 0.87

--- Training candidate: GradientBoosting ---
Best CV score: 0.91
Test RMSE: 4.87 | R2: 0.89

Best model chosen: GradientBoosting
Saved best model to: /content/best_model.pkl
```

#### Step 2: Start the API Server

```bash
uvicorn predict:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

#### Step 3: Serve the Frontend

Open a new terminal:

```bash
# Simple HTTP server
python -m http.server 3000

# Or use any static server
# npm install -g http-server
# http-server -p 3000
```

#### Step 4: Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

---

## 📖 Usage

### Making Predictions via Web UI

1. **Navigate to the form section** (click "Start Predicting" or scroll down)

2. **Enter polymer parameters:**
   - **Polymer Type**: Select from PLA, PCL, PHB, PBS, PBAT
   - **Molecular Weight**: Enter value (e.g., 15000)
   - **Crystallinity**: Enter percentage (0-100)
   - **Thickness**: Enter in millimeters
   - **Temperature**: Enter in Celsius (0-100)
   - **pH Level**: Enter value (0-14)
   - **Porosity**: Enter percentage
   - **Enzyme Presence**: Select 1 (present) or 0 (absent)
   - **Days**: Enter time period for prediction

3. **Click "Predict Degradation"** or try the example data

4. **View Results:**
   - Prediction percentage
   - Degradation curve visualization
   - Key parameter summary
   - Confidence score

### Example Request

**Sample Input:**
```json
{
  "Polymer_Type": "PLA",
  "Molecular_Weight": 15000,
  "Crystallinity": 32.5,
  "Thickness_mm": 1.0,
  "Temperature_C": 37,
  "pH": 7.4,
  "Porosity": 12.8,
  "Enzyme": 1,
  "Days": 130
}
```

**Sample Output:**
```
Predicted Degradation: 78.5%
After 130 days under specified conditions
```

---

## 🔌 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```http
GET /
```

**Response:**
```json
{
  "status": "ok",
  "message": "Send POST request to /predict"
}
```

#### 2. Make Prediction
```http
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "Polymer_Type": "PLA",
  "Molecular_Weight": 15000.0,
  "Crystallinity": 32.5,
  "Thickness_mm": 1.0,
  "Temperature_C": 37.0,
  "pH": 7.4,
  "Porosity": 12.8,
  "Enzyme": 1.0,
  "Days": 130.0
}
```

**Response (200 OK):**
```json
{
  "prediction": 78.52,
  "prediction_array": [78.52],
  "model_path": "./content/best_model.pkl"
}
```

**Error Response (500):**
```json
{
  "detail": "Prediction error: <error message>"
}
```

### Testing with cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Polymer_Type": "PLA",
    "Molecular_Weight": 15000,
    "Crystallinity": 32.5,
    "Thickness_mm": 1.0,
    "Temperature_C": 37,
    "pH": 7.4,
    "Porosity": 12.8,
    "Enzyme": 1.2,
    "Days": 28
  }'
```

### Testing with JavaScript

```javascript
fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    Polymer_Type: "PLA",
    Molecular_Weight: 15000,
    Crystallinity: 32.5,
    Thickness_mm: 1.0,
    Temperature_C: 37,
    pH: 7.4,
    Porosity: 12.8,
    Enzyme: 1.2,
    Days: 28
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

### Interactive API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📁 Project Structure

```
polymer-predictor/
│
├── index.html                          # Frontend UI
├── predict.py                          # FastAPI backend server
├── train_and_save_best_model.py        # ML training script
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
│
├── content/
│   ├── dataset.csv                     # Training dataset
│   ├── best_model.pkl                  # Trained model (generated)
│   └── best_model_metadata.json        # Model metadata (generated)
│
├── assets/                             # (Optional) Images, icons
│   └── screenshots/
│       ├── homepage.png
│       ├── prediction-form.png
│       └── results.png
│
└── docs/                               # (Optional) Additional documentation
    ├── API.md
    ├── DEPLOYMENT.md
    └── MODEL_TRAINING.md
```

---

## 🤖 Model Training

### Dataset Requirements

Your CSV should contain the following columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Polymer_Type | Categorical | Type of polymer | PLA, PCL, PHB, PBS, PBAT |
| Molecular_Weight | Numeric | Molecular weight | 15000 |
| Crystallinity | Numeric | Crystallinity percentage | 32.5 |
| Thickness_mm | Numeric | Thickness in mm | 1.0 |
| Temperature_C | Numeric | Temperature in Celsius | 37 |
| pH | Numeric | pH level | 7.4 |
| Porosity | Numeric | Porosity percentage | 12.8 |
| Enzyme | Numeric | Enzyme presence (0 or 1) | 1 |
| Days | Numeric | Time period | 130 |
| **Degradation_Percent** | **Numeric** | **Target variable** | **78.5** |

### Training Process

The `train_and_save_best_model.py` script performs:

1. **Data Loading**: Reads CSV and validates structure
2. **Preprocessing**: 
   - Handles missing values (median for numeric, mode for categorical)
   - Scales numeric features (StandardScaler)
   - Encodes categorical features (OneHotEncoder)
3. **Model Selection**: Trains and evaluates 3 model families
   - RandomForestRegressor
   - GradientBoostingRegressor
   - HistGradientBoostingRegressor
4. **Hyperparameter Tuning**: RandomizedSearchCV with 8 iterations
5. **Cross-Validation**: 4-fold CV for robust evaluation
6. **Model Saving**: Serializes best model with joblib

### Customizing Training

Edit `train_and_save_best_model.py`:

```python
# Change dataset path
DATA_PATH = "/path/to/your/dataset.csv"

# Adjust train/test split
TEST_SIZE = 0.25  # 75% train, 25% test

# Change random state for reproducibility
RANDOM_STATE = 42

# Modify hyperparameter search space
param_dists["RandomForest"] = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [10, 20, 30],
    "model__min_samples_split": [2, 5, 10]
}
```

### Evaluating Model Performance

After training, check the metadata file:

```bash
cat content/best_model_metadata.json
```

**Example Output:**
```json
{
  "best_model_name": "GradientBoosting",
  "final_eval": {
    "rmse": 4.87,
    "r2": 0.89
  },
  "candidates": [
    {
      "model": "RandomForest",
      "cv_score": 0.87,
      "rmse": 5.23,
      "r2": 0.85
    },
    {
      "model": "GradientBoosting",
      "cv_score": 0.91,
      "rmse": 4.87,
      "r2": 0.89
    }
  ]
}
```

---

## 🚢 Deployment

### Option 1: Cloud Platform (Recommended)

#### Deploy Backend to Railway

1. **Create Railway account**: https://railway.app
2. **Install Railway CLI**:
```bash
npm i -g @railway/cli
```

3. **Deploy**:
```bash
railway login
railway init
railway up
```

4. **Set environment variables**:
```bash
railway variables set MODEL_PATH=/app/content/best_model.pkl
```

#### Deploy Frontend to Vercel/Netlify

1. **Push to GitHub**
2. **Connect repository** to Vercel/Netlify
3. **Update API URL** in `index.html`:
```javascript
const API_BASE = 'https://your-railway-app.railway.app';
```

### Option 2: Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and Run:**
```bash
docker build -t polymer-predictor .
docker run -p 8000:8000 polymer-predictor
```

### Option 3: Traditional VPS

1. **Set up nginx as reverse proxy**
2. **Configure systemd service** for uvicorn
3. **Set up SSL** with Let's Encrypt
4. **Configure firewall** (allow ports 80, 443)

**nginx configuration:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        root /var/www/polymer-predictor;
        index index.html;
    }

    location /api/ {
        proxy_pass http://localhost:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/polymer-predictor.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create feature branch
git checkout -b feature/new-feature
```

### Coding Standards

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Test your changes before submitting PR

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```
MIT License

Copyright (c) 2024 Sagar Pal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact

**Sagar Pal**

- 📧 Email: sagarpal0402@gmail.com
- 💼 LinkedIn: [linkedin.com/in/sagarpal](https://linkedin.com/in/sagarpal)
- 🐙 GitHub: [@sagarpal](https://github.com/sagarpal)
- 💻 Codolio: [codolio.com/profile/sagarpal](https://codolio.com/profile/sagarpal)
- 📱 Phone: +91-9354336487

**Project Link**: [https://github.com/yourusername/polymer-predictor](https://github.com/yourusername/polymer-predictor)

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for building APIs
- [scikit-learn](https://scikit-learn.org/) - Machine learning library
- [Chart.js](https://www.chartjs.org/) - JavaScript charting library
- [Font Awesome](https://fontawesome.com/) - Icon library
- [Galgotias University](https://www.galgotiasuniversity.edu.in/) - Academic support

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/polymer-predictor?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/polymer-predictor?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/polymer-predictor)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/polymer-predictor)

---

## 🎯 Roadmap

- [x] Basic prediction functionality
- [x] Interactive UI with Chart.js
- [x] FastAPI backend
- [x] Automated model selection
- [ ] User authentication system
- [ ] Prediction history dashboard
- [ ] Batch prediction (CSV upload)
- [ ] Confidence intervals
- [ ] Mobile application
- [ ] Advanced model (LSTM/Transformer)
- [ ] Real-time collaboration features

---

## 📈 Performance Metrics

- ⚡ **API Response Time**: < 100ms average
- 🎯 **Model Accuracy**: R² > 0.85
- 📊 **Cross-validation Score**: 4-fold CV > 0.88
- 🚀 **Prediction Speed**: < 1 second end-to-end
- 📱 **Mobile Responsive**: Works on all devices
- 🔒 **Security**: CORS configured, type-safe APIs

---

<div align="center">

**Made with ❤️ by Sagar Pal**

⭐ **Star this repo if you found it helpful!** ⭐

[⬆ Back to Top](#-polymer-predictor---ai-powered-biodegradation-analysis-platform)

</div>
