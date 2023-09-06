from lullaby_api.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("lullaby_api.tasks.example",)
