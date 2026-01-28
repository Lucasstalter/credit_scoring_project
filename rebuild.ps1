# rebuild.ps1 - Rebuild completo do projeto
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  REBUILD COMPLETO DO PROJETO" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/4] Parando containers..." -ForegroundColor Yellow
docker-compose down
Write-Host "✓ Containers parados" -ForegroundColor Green
Write-Host ""

Write-Host "[2/4] Removendo imagens antigas..." -ForegroundColor Yellow
docker-compose down --rmi local 2>$null
Write-Host "✓ Imagens removidas" -ForegroundColor Green
Write-Host ""

Write-Host "[3/4] Rebuilding (isso pode demorar)..." -ForegroundColor Yellow
docker-compose build --no-cache
Write-Host "✓ Build completo!" -ForegroundColor Green
Write-Host ""

Write-Host "[4/4] Iniciando serviços..." -ForegroundColor Yellow
docker-compose up -d
Start-Sleep -Seconds 5
Write-Host "✓ Serviços iniciados!" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  STATUS DOS SERVIÇOS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
docker-compose ps
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host "  TUDO PRONTO!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "API:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para testar:" -ForegroundColor Yellow
Write-Host "  docker-compose run --rm api pytest tests/ -v" -ForegroundColor White
