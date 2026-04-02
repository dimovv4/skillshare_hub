import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillshare_hub.settings")

app = Celery("skillshare_hub")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
