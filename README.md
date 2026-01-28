# Credit Scoring System

A production-ready credit scoring system powered by machine learning, featuring an XGBoost model trained on real financial data to predict credit default risk with 86.87% AUC-ROC accuracy.

Link: https://credit-scoring-project.vercel.app/

## Overview

This project implements an end-to-end credit scoring solution that analyzes customer financial data to assess credit risk in real-time. The system combines advanced machine learning techniques with a modern web interface and RESTful API.

### Key Features

- **High Accuracy Model**: XGBoost classifier achieving 86.87% AUC-ROC on real-world data
- **Real-Time Predictions**: Sub-100ms response time for credit assessments
- **Production Ready**: Containerized with Docker, automated testing, and comprehensive monitoring
- **Modern Interface**: Clean, responsive web UI for credit analysis
- **Scalable Architecture**: FastAPI backend with MongoDB for data persistence

## Tech Stack

**Machine Learning**
- Python 3.11
- XGBoost 2.0.3
- scikit-learn 1.4.0
- pandas, numpy

**Backend**
- FastAPI (REST API)
- MongoDB (data storage)
- Docker & Docker Compose

**Frontend**
- HTML5, CSS3, JavaScript
- Responsive design
- Real-time form validation

**DevOps**
- Docker containerization
- Automated testing with pytest
- CI/CD ready

## Model Performance

The model was trained on the "Give Me Some Credit" dataset from Kaggle, containing 150,000 real credit records.

| Metric | Value |
|--------|-------|
| AUC-ROC | 0.8687 |
| Precision | 22.56% |
| Recall | 76.76% |
| Training Samples | 150,000 |
| Features | 15 |

The model prioritizes high recall to minimize false negatives (missed defaults), which is critical for financial risk management.


## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/credit-scoring.git
cd credit-scoring
```

2. Download the dataset

Download the "Give Me Some Credit" dataset from [Kaggle](https://www.kaggle.com/c/GiveMeSomeCredit/data) and extract `cs-training.csv` to `data/raw/`.

3. Build and start services
```bash
docker-compose build
docker-compose up -d
```

4. Train the model
```bash
# Windows
powershell -ExecutionPolicy Bypass -File .\train_real.ps1

# Linux/Mac
python train_real_data.py
```

5. Access the application

- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Usage

### Web Interface

1. Open http://localhost:8000 in your browser
2. Fill in the customer financial information
3. Click "Analisar crédito" to get instant credit assessment
4. Review the risk score and recommendation

### API

Make predictions programmatically using the REST API:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "CLI001",
    "idade": 35,
    "renda_mensal": 5000,
    "divida_total": 15000,
    "limite_credito": 10000,
    "saldo_utilizado": 7000,
    "valor_parcela": 500,
    "idade_credito_meses": 60,
    "tempo_emprego_meses": 24,
    "atrasos_30d": 1,
    "atrasos_90d": 0,
    "pagamentos_dia": 11,
    "renda_std_6m": 200
  }'
```

Response:
```json
{
  "customer_id": "CLI001",
  "score": 0.235,
  "risk_category": "BAIXO",
  "approved": true,
  "limit_recommended": 15000,
  "timestamp": "2026-01-27T12:00:00"
}
```

## Development

### Local Setup

1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

3. Run tests
```bash
pytest tests/
```

### Model Training

To retrain the model with updated data:
```bash
python train_real_data.py
```

This will:
- Load and preprocess the dataset
- Perform feature engineering
- Train the XGBoost model
- Evaluate performance metrics
- Save the model to `models/production/`

### Running Without Docker
```bash
# Start API
uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000

# Open frontend/index.html in browser
```

## Model Details

### Features

The model uses 15 engineered features:

**Financial Metrics**
- Monthly income
- Total debt
- Debt ratio
- Credit utilization
- Payment amounts

**Credit History**
- Credit age (months)
- Employment tenure
- Late payments (30-59, 60-89, 90+ days)
- On-time payments

**Derived Features**
- Income volatility
- Income-to-debt ratio
- High utilization flag

### Algorithm

XGBoost (Extreme Gradient Boosting) with the following configuration:

- Objective: Binary classification
- Evaluation metric: AUC-ROC
- Max depth: 6
- Learning rate: 0.05
- Scale pos weight: 13.96 (to handle class imbalance)
- Early stopping: 50 rounds

### Training Process

1. Data cleaning and outlier treatment
2. Feature engineering
3. Train/test split (80/20, stratified)
4. Model training with early stopping
5. Performance evaluation
6. Model serialization

## API Reference

### Endpoints

#### `GET /`
Returns service information and status.

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-27T12:00:00"
}
```

#### `POST /predict`
Predicts credit risk for a customer.

**Request Body:**
- `customer_id` (string): Customer identifier
- `idade` (integer): Age (18-100)
- `renda_mensal` (float): Monthly income
- `divida_total` (float): Total debt
- `limite_credito` (float): Credit limit
- `saldo_utilizado` (float): Used credit
- `valor_parcela` (float): Payment amount
- `idade_credito_meses` (integer): Credit age in months
- `tempo_emprego_meses` (integer): Employment tenure
- `atrasos_30d` (integer): 30-59 day late payments
- `atrasos_90d` (integer): 90+ day late payments
- `pagamentos_dia` (integer): On-time payments (0-12)
- `renda_std_6m` (float): Income volatility

**Response:**
- `customer_id`: Customer identifier
- `score`: Risk score (0-1, higher = riskier)
- `risk_category`: BAIXO, MEDIO, or ALTO
- `approved`: Boolean approval decision
- `limit_recommended`: Recommended credit limit
- `timestamp`: Prediction timestamp

## Testing

Run the test suite:
```bash
# All tests
pytest

# With coverage
pytest --cov=src tests/

# Specific test file
pytest tests/test_api.py
```

## Data

This project uses the "Give Me Some Credit" dataset from Kaggle, containing anonymized credit bureau data.

**Dataset Statistics:**
- 150,000 customer records
- 11 original features
- 6.68% default rate
- Real-world financial data

**Note:** The dataset is not included in this repository due to size constraints. Download it from [Kaggle](https://www.kaggle.com/c/GiveMeSomeCredit/data).

## Deployment

### Production Checklist

- [ ] Environment variables configured
- [ ] Database backups enabled
- [ ] Monitoring and logging setup
- [ ] Rate limiting configured
- [ ] HTTPS enabled
- [ ] CORS policies reviewed
- [ ] Model versioning implemented

### Deploy to Cloud

The application is designed to be deployed on platforms like:

- **Railway**: Easy Docker deployment
- **AWS**: ECS, Fargate, or EC2
- **Google Cloud**: Cloud Run or GKE
- **Azure**: Container Instances or AKS

Example Railway deployment:
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway up
```

## Performance Considerations

- **Prediction Latency**: <100ms average
- **Throughput**: Scales horizontally with Docker
- **Memory**: ~500MB per container
- **Model Size**: ~2MB serialized

## Limitations

- Model trained on US credit data (may not generalize globally)
- Threshold tuning required for production deployment
- Class imbalance affects precision metrics
- No real-time model retraining


## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Acknowledgments

- Dataset: "Give Me Some Credit" Kaggle competition
- XGBoost: Tianqi Chen and Carlos Guestrin
- FastAPI: Sebastián Ramírez

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with Python, XGBoost, FastAPI, and Docker**
