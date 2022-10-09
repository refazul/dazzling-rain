# Start Project

```
docker compose run --rm django django-admin startproject projectname .
```

# MySQL settings
### File: projectname > settings.py

```
import os

....

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': 'db',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB'
        }
    }
}
```


# Run Migration

```
docker compose run --rm django python manage.py migrate
```

# Create Superuser

```
docker compose run --rm django python manage.py createsuperuser
```

# Create App

```
docker compose run --rm django python manage.py startapp report
```

# Create Model
### File: report > models.py

```

```