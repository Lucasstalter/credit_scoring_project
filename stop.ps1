# stop.ps1 - Stop services
Write-Host "Stopping services..." -ForegroundColor Yellow
docker-compose down
Write-Host "Services stopped!" -ForegroundColor Green
