# Setup no Windows

## Pré-requisitos

1. **Docker Desktop for Windows**
   - Download: https://www.docker.com/products/docker-desktop
   - Instale e reinicie o computador
   - Certifique-se que está rodando

2. **PowerShell** (já vem no Windows)

## Instalação

1. Extrair o ZIP
2. Abrir PowerShell na pasta do projeto
3. Executar os comandos abaixo

## Comandos PowerShell

### Build
```powershell
.\build.ps1
# OU
docker-compose build
```

### Deploy
```powershell
.\deploy.ps1
# OU
docker-compose up -d
```

### Ver logs
```powershell
.\logs.ps1
# OU
docker-compose logs -f api
```

### Parar serviços
```powershell
.\stop.ps1
# OU
docker-compose down
```

### Rodar testes
```powershell
.\test.ps1
# OU
docker-compose run --rm api pytest tests/ -v
```

### Limpar tudo
```powershell
.\clean.ps1
# OU
docker-compose down -v
```

## Quick Start

```powershell
# 1. Build
docker-compose build

# 2. Iniciar
docker-compose up -d

# 3. Verificar
docker-compose ps

# 4. Acessar
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

## Testar API

### PowerShell
```powershell
# Health check
Invoke-WebRequest -Uri http://localhost:8000/health

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

### Ou use o navegador
Abra: http://localhost:8000/docs

## Desenvolvimento Local (sem Docker)

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Rodar API
uvicorn src.api.app:app --reload

# Rodar testes
pytest tests/ -v
```

## Troubleshooting

### Erro: "docker-compose não é reconhecido"
- Certifique-se que Docker Desktop está rodando
- Reinicie o PowerShell
- Verifique: `docker --version`

### Erro: "Porta 8000 já está em uso"
```powershell
# Ver o que está usando a porta
netstat -ano | findstr :8000

# Matar o processo (substitua PID)
taskkill /PID <numero_do_pid> /F
```

### Scripts não executam
```powershell
# Habilitar execução de scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Docker muito lento
- Alocar mais memória no Docker Desktop (Settings > Resources)
- Mínimo recomendado: 4GB RAM

## Verificar se está funcionando

```powershell
# Ver containers rodando
docker-compose ps

# Ver logs
docker-compose logs api

# Testar API
Invoke-WebRequest http://localhost:8000/health
```

## Próximos Passos

1. ✅ Extrair projeto
2. ✅ Instalar Docker Desktop
3. ✅ Rodar `docker-compose up -d`
4. ✅ Acessar http://localhost:8000/docs
5. ✅ Testar predições

Boa sorte! 🚀
