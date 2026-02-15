from flask import Flask
from celery import Celery
import time

app = Flask(__name__)

# Initialize Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

# Flask Configuration for Celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',  
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery = make_celery(app)

@app.route('/health')
def health():
    return "Service is running", 200

@app.route('/update_timestamp')
def update_timestamp():
    task = update_today_records.apply_async()
    return f'Timestamp update task is running with task ID: {task.id}', 202

@celery.task
def update_today_records():
    time.sleep(5)  # Simulate a task that takes time
    print("Updated timestamp for today's records.")
    return 'Timestamp updated successfully'

if __name__ == '__main__':
    app.run(debug=True)

