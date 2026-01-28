# train_real.ps1 - Treinar com dataset real do Kaggle

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TREINAMENTO COM DADOS REAIS" -ForegroundColor Cyan  
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se arquivo existe
if (!(Test-Path "data\raw\cs-training.csv")) {
    Write-Host "Erro: Dataset nao encontrado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Baixe o dataset em:" -ForegroundColor Yellow
    Write-Host "  https://www.kaggle.com/c/GiveMeSomeCredit/data" -ForegroundColor White
    Write-Host ""
    Write-Host "Extraia o arquivo cs-training.csv para:" -ForegroundColor Yellow
    Write-Host "  data\raw\cs-training.csv" -ForegroundColor White
    Write-Host ""
    exit 1
}

Write-Host "Dataset encontrado!" -ForegroundColor Green
Write-Host ""

Write-Host "Treinando modelo com dados reais..." -ForegroundColor Yellow
docker-compose exec api python train_real_data.py

Write-Host "`nReiniciando API com novo modelo..." -ForegroundColor Yellow
docker-compose restart api
Start-Sleep -Seconds 3

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  MODELO REAL TREINADO!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Teste a API:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000/docs" -ForegroundColor White
Write-Host ""