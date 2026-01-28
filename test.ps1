# test.ps1 - Run tests
Write-Host "Running tests..." -ForegroundColor Green
docker-compose run --rm api pytest tests/ -v
