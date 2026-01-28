# clean.ps1 - Clean up everything
Write-Host "Cleaning up..." -ForegroundColor Yellow
docker-compose down -v
docker system prune -f
Write-Host "Cleanup complete!" -ForegroundColor Green
