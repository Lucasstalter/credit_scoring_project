# deploy.ps1 - Deploy services
Write-Host "Deploying services..." -ForegroundColor Green
docker-compose up -d
Start-Sleep -Seconds 5
docker-compose ps
Write-Host "`nServices started!" -ForegroundColor Green
Write-Host "API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Docs: http://localhost:8000/docs" -ForegroundColor Cyan
