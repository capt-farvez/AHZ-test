# AHZ-test

To Run Projects:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
To use Celery:
```
celery -A celery_worker worker --loglevel=info
``
