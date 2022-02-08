start:
	docker-compose up -d

down:
	docker-compose down

test:
	docker-compose -f docker-compose.test.yml up --build

