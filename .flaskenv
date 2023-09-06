FLASK_ENV=development
FLASK_APP="app:create_app"
SECRET_KEY=changeme
DATABASE_URI="sqlite:///lullaby_api.db"
CELERY_BROKER_URL=amqp://guest:guest@localhost/  # only present when celery is enabled
CELERY_RESULT_BACKEND_URL=amqp://guest:guest@localhost/  # only present when celery is enabled
