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

## Usage 🚀
## Web Application
bash
python app.py
Visit http://localhost:5000 in your browser

## Api Connection
bash
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

## Tech Stack 🧰
Frontend: HTML5, CSS3, JavaScript

Backend: Python, Flask

ML Framework: scikit-learn

NLP: NLTK, TF-IDF Vectorization

Database: SQLite (for prediction history)

Deployment: Render, Gunicorn

## Model Architecture 🤖
mermaid
graph TD
    A[Raw Text] --> B[Text Preprocessing]
    B --> C[TF-IDF Vectorization]
    C --> D[SVM Classifier]
    D --> E[Prediction]
Preprocessing Steps:

1.Lowercasing

2.Tokenization

3.Stopword Removal

4.Lemmatization

5.Special Character Removal

## Performance Metrics

Metric	Score
Accuracy	98.2%
Precision	98.5%
Recall	97.8%
F1-Score	98.1%

API Documents 📚
Endpoints:

POST /api/predict - Classify SMS message

GET /api/history - Get prediction history

Request Format:
{
  "message": "Your SMS text here"
}
Response Format:

json
{
  "prediction": "spam/ham",
  "confidence": 0.000-1.000,
  "timestamp": "YYYY-MM-DD HH:MM:SS"
}

## Deployement 🌐
Deployed on Render with:

1.Web Service: Gunicorn WSGI server

2.Runtime: Python 3.9.16

3.Auto-deploy: GitHub integration

4.Environment Variables:

5.PYTHON_VERSION=3.9.16

6.FLASK_ENV=production

## Contributing 🤝
1.Fork the repository

2.Create feature branch: git checkout -b feature/new-feature

3.Commit changes: git commit -m 'Add awesome feature'

4.Push to branch: git push origin feature/new-feature

5.Open Pull Request

## Lisence 📄
Distributed under MIT License. See LICENSE for details.

## Contact 📧
Jitendra Srivastava

GitHub: @JitendraSrivastava12

LinkedIn: jitendra-srivastava

Email: jitendra.ug23@nitp.ac.in
