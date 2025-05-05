from celery import Celery
from celery.schedules import crontab
from .tasks import archive_old_books
app = Celery('book_tasks', broker='redis://localhost:6379/0')
app.conf.beat_schedule = {
    'archive-old-books-every-30-minutes': {
        'task': 'tasks.archive_old_books',
        'schedule': crontab(minute='*/30'),  # Every 30 minutes
    },
}
app.conf.timezone = 'UTC'