# Correções Rápidas

## Erro: "pytest: executable file not found"

### Solução:

Rebuild a imagem Docker:

```powershell
# 1. Parar containers
docker-compose down

# 2. Rebuild (força reconstrução)
docker-compose build --no-cache

# 3. Subir novamente
docker-compose up -d

# 4. Agora os testes funcionam
docker-compose run --rm api pytest tests/ -v
```

## Ou rodar testes SEM Docker:

```powershell
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar
.\venv\Scripts\Activate.ps1

# 3. Instalar dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Rodar testes
pytest tests/ -v
```

## Rodar APENAS a API (sem testes):

```powershell
# Rebuild apenas o necessário
docker-compose build api

# Subir
docker-compose up -d

# Acessar
# http://localhost:8000/docs
```

## Comandos úteis:

```powershell
# Ver logs se algo der errado
docker-compose logs -f api

# Ver containers rodando
docker-compose ps

# Reiniciar tudo do zero
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Testar a API manualmente:

### Pelo navegador:
1. Abra: http://localhost:8000/docs
2. Teste os endpoints por lá

### Pelo PowerShell:
```powershell
# Health check
Invoke-WebRequest http://localhost:8000/health

# Predição
$body = @{
    customer_id = "TEST001"
    idade = 35
    renda_mensal = 5000
    divida_total = 15000
    limite_credito = 10000
    saldo_utilizado = 7000
    valor_parcela = 500
    idade_credito_meses = 60
    tempo_emprego_meses = 24
    atrasos_30d = 1
    atrasos_90d = 0
    pagamentos_dia = 11
    renda_std_6m = 200
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:8000/predict -Method Post -Body $body -ContentType "application/json"
```

## Avisar sobre a versão do docker-compose.yml:

O warning sobre `version` é obsoleto pode ser ignorado. Mas se quiser remover:

Edite `docker-compose.yml` e remova a linha:
```yaml
version: '3.8'
```

Deixe apenas:
```yaml
services:
  api:
    ...
```
