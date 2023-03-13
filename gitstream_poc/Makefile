.PHONY: start stop restart

start:
	docker-compose up -d --build

stop:
	docker-compose down

restart:
	docker-compose down
	docker-compose up -d --build

runserver:
	docker-compose exec web python manage.py runserver 0.0.0.0:8000

makemigrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser