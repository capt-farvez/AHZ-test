from celery import Celery
from datetime import datetime, timedelta
from .models import Session, Book  # Import your database session and Book model
app = Celery('book_tasks', broker='redis://localhost:6379/0')
@app.task
def archive_old_books():
    session = Session()  # Create a new session
    ten_years_ago = datetime.now() - timedelta(days=365 * 10)
    
    # Query books that haven't been updated in over 10 years
    old_books = session.query(Book).filter(
        Book.last_updated < ten_years_ago,
        Book.is_archived == False
    ).all()
    
    # Update the is_archived field for those books
    for book in old_books:
        book.is_archived = True
    
    session.commit()  # Commit the changes
    session.close()  # Close the session