from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Credit Scoring API",
    description="API para previsão de risco de crédito",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CreditApplication(BaseModel):
    customer_id: str
    idade: int = Field(..., ge=18, le=100)
    renda_mensal: float = Field(..., gt=0)
    divida_total: float = Field(..., ge=0)
    limite_credito: float = Field(..., ge=0)
    saldo_utilizado: float = Field(..., ge=0)
    valor_parcela: float = Field(..., ge=0)
    idade_credito_meses: int = Field(..., ge=0)
    tempo_emprego_meses: int = Field(..., ge=0)
    atrasos_30d: int = Field(..., ge=0)
    atrasos_90d: int = Field(..., ge=0)
    pagamentos_dia: int = Field(..., ge=0)
    renda_std_6m: float = Field(..., ge=0)

class PredictionResponse(BaseModel):
    customer_id: str
    score: float
    risk_category: str
    approved: bool
    limit_recommended: Optional[float]
    timestamp: str

@app.get("/")
async def root():
    return {
        "service": "Credit Scoring API",
        "version": "1.0.0",
        "status": "online"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(application: CreditApplication):
    # Simulação de predição (modelo simplificado)
    # Calcular score baseado em regras simples
    score = 0.0
    
    # Penalizar atrasos
    if application.atrasos_90d > 0:
        score += 0.4
    elif application.atrasos_30d > 0:
        score += 0.2
    
    # Penalizar alta utilização de crédito
    utilizacao = application.saldo_utilizado / (application.limite_credito + 1)
    if utilizacao > 0.8:
        score += 0.15
    
    # Penalizar alta razão dívida/renda
    razao_divida = application.divida_total / (application.renda_mensal * 12 + 1)
    if razao_divida > 0.5:
        score += 0.15
    
    # Limitar entre 0 e 1
    score = min(score, 1.0)
    
    # Determinar categoria e aprovação
    if score < 0.3:
        risk_category = "BAIXO"
        approved = True
        limit_recommended = application.renda_mensal * 3
    elif score < 0.6:
        risk_category = "MEDIO"
        approved = True
        limit_recommended = application.renda_mensal * 1.5
    else:
        risk_category = "ALTO"
        approved = False
        limit_recommended = 0
    
    return PredictionResponse(
        customer_id=application.customer_id,
        score=score,
        risk_category=risk_category,
        approved=approved,
        limit_recommended=limit_recommended,
        timestamp=datetime.utcnow().isoformat()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)