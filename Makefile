loc-run:
	docker-compose -f docker-compose-loc.yml up
loc-stop:
	docker-compose -f docker-compose-loc.yml stop
loc-build:
	docker-compose -f docker-compose-loc.yml build
loc-migrate:
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py makemigrations 
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py migrate
loc-requirements:
	docker-compose -f docker-compose-loc.yml run --rm django pip install -r requirements.txt
loc-statics:
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py collectstatic --no-input 
loc-superuser:
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py createsuperuser 
loc-reset:
	docker-compose -f docker-compose-loc.yml down -v
	rm -rf .pgdata/
loc-test:
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py test --settings=api_pairgame.settings.local
loc-startapp:
	docker-compose -f docker-compose-loc.yml run --rm django ./manage.py startapp $(name)
	sudo chmod 777 -R ./src/$(name)
loc-restart:
	docker-compose -f docker-compose-loc.yml restart $(name)
pro-run:
	docker-compose -f docker-compose-pro.yml up
pro-stop:
	docker-compose -f docker-compose-pro.yml stop
pro-build:
	docker-compose -f docker-compose-pro.yml build
pro-migrate:
	docker-compose -f docker-compose-pro.yml run --rm django ./manage.py makemigrations 
	docker-compose -f docker-compose-pro.yml run --rm django ./manage.py migrate
pro-requirements:
	docker-compose -f docker-compose-pro.yml run --rm django pip install -r requirements.txt
pro-statics:
	docker-compose -f docker-compose-pro.yml run --rm django ./manage.py collectstatic --no-input 
pro-superuser:
	docker-compose -f docker-compose-pro.yml run --rm django ./manage.py createsuperuser 
pro-reset:
	docker-compose -f docker-compose-pro.yml down -v
	rm -rf .pgdata/
pro-test:
	docker-compose -f docker-compose-pro.yml run --rm django ./manage.py test --settings=api_pairgame.settings.production
pro-restart:
	docker-compose -f docker-compose-pro.yml restart $(name)
clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*