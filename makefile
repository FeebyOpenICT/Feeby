start:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

logs:
	docker compose logs -f

debug:
	docker compose -f docker-compose.yml -f docker-compose.debug.yml up -d

debug-build:
	docker compose -f docker-compose.yml -f  docker-compose.debug.yml build

debug-down:
	docker compose -f docker-compose.yml -f  docker-compose.debug.yml down

debug-logs:
	docker compose -f docker-compose.yml -f  docker-compose.debug.yml logs -f

prod-start:
	docker compose -f docker-compose.yml -f  docker-compose.prod.yml up -d --build

prod-build:
	docker compose -f docker-compose.yml -f  docker-compose.prod.yml build

prod-down:
	docker compose -f docker-compose.yml -f  docker-compose.prod.yml down

prod-logs:
	docker compose -f docker-compose.yml -f  docker-compose.prod.yml logs -f

pytest-backend:
	docker compose -f docker-compose.yml -f docker-compose.test.yml up backend | tee test_backend_log.txt
	docker compose logs backend 
