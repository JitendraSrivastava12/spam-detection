# SMS Spam Classifier 🛡️

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![GitHub Stars](https://img.shields.io/github/stars/JitendraSrivastava12/spam-detection?style=social)]()

**Live Demo:** https://spam-detection-jituji.onrender.com/

A machine learning-powered web application that identifies spam SMS messages with 98.2% accuracy, built with Python and Flask.

## Table of Contents
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Tech Stack](#tech-stack-)
- [Model Architecture](#model-architecture-)
- [API Documentation](#api-documentation-)
- [Deployment](#deployment-)
- [Contributing](#contributing-)
- [License](#license-)
- [Contact](#contact-)

## Features ✨
- Real-time spam/ham classification
- Probability confidence score display
- Responsive web interface
- REST API endpoint
- Message prediction history
- Cross-platform compatibility
- Error handling and validation

## Installation ⚙️

### Prerequisites
- Python 3.9+
- pip package manager

### Steps
1. Clone repository:
git clone https://github.com/JitendraSrivastava12/spam-detection.git
cd spam-detection

2.Create virtual environment:
bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

3. Install dependencies:

bash
pip install -r requirements.txt

4.Download NLTK data:
bash
python -m nltk.downloader punkt wordnet omw-1.4 stopwords

<h1>Usage<h1? 🚀
Web Application
bash
Copy
python app.py
Visit http://localhost:5000 in your browser

API Endpoint
bash
Copy
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"message":"WINNER!! You won 10 lakh rupees!"}'
Response:

json
Copy
{
  "prediction": "spam",
  "confidence": 0.982,
  "status": 200
}
Tech Stack 🧰
Frontend: HTML5, CSS3, JavaScript

Backend: Python, Flask

ML Framework: scikit-learn

NLP: NLTK, TF-IDF Vectorization

Database: SQLite (for prediction history)

Deployment: Render, Gunicorn

Model Architecture 🤖
mermaid
Copy
graph TD
    A[Raw Text] --> B[Text Preprocessing]
    B --> C[TF-IDF Vectorization]
    C --> D[SVM Classifier]
    D --> E[Prediction]
Preprocessing Steps:

Lowercasing

Tokenization

Stopword Removal

Lemmatization

Special Character Removal

Performance Metrics:

Metric	Score
Accuracy	98.2%
Precision	98.5%
Recall	97.8%
F1-Score	98.1%
API Documentation 📚
Endpoints:

POST /api/predict - Classify SMS message

GET /api/history - Get prediction history

Request Format:

json
Copy
{
  "message": "Your SMS text here"
}
Response Format:

json
Copy
{
  "prediction": "spam/ham",
  "confidence": 0.000-1.000,
  "timestamp": "YYYY-MM-DD HH:MM:SS"
}
Deployment 🌐
Deployed on Render with:

Web Service: Gunicorn WSGI server

Runtime: Python 3.9.16

Auto-deploy: GitHub integration

Environment Variables:

PYTHON_VERSION=3.9.16

FLASK_ENV=production

Contributing 🤝
Fork the repository

Create feature branch: git checkout -b feature/new-feature

Commit changes: git commit -m 'Add awesome feature'

Push to branch: git push origin feature/new-feature

Open Pull Request

License 📄
Distributed under MIT License. See LICENSE for details.

Contact 📧
Jitendra Srivastava

GitHub: @JitendraSrivastava12

LinkedIn: jitendra-srivastava

Email: jitendra.ug23@nitp.ac.in
