# logs.ps1 - View logs
param(
    [string]$Service = "api"
)
docker-compose logs -f $Service
