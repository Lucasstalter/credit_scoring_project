# build.ps1 - Build Docker images
Write-Host "Building Docker images..." -ForegroundColor Green
docker-compose build
Write-Host "Build complete!" -ForegroundColor Green
