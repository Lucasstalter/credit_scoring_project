.PHONY: help build deploy test

help:
	@echo "make build  - Build Docker images"
	@echo "make deploy - Deploy services"
	@echo "make test   - Run tests"
	@echo "make stop   - Stop services"

build:
	docker-compose build

deploy:
	docker-compose up -d

test:
	pytest tests/ -v

stop:
	docker-compose down

clean:
	docker-compose down -v
