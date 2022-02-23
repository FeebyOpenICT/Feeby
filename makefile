start:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

test:
	docker-compose -f docker-compose.test.yml up --build

prod-start:
	docker-compose -f docker-compose.prod.yml up -d --build

prod-down:
	docker-compose -f docker-compose.prod.yml down

prod-logs:
	docker-compose -f docker-compose.prod.yml logs -f

logs:
	docker-compose logs -f

database-start:
	docker-compose up -d db adminer traefik
