# Pantry

Pantry is a Django application which use postgres as a database. Main purpose of this application is to make life easier when governing list of things to buy at the grocery.
Detailed instruction of how to use app is described under "about" tab in the app.

## Installation

To make app run locally on your computer first install and configure postgres database. Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install /path/to/requirements.txt
```

After successful install of the packages from requirement.txt file setup database connection in /pantry/settings.py
 
 ```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost'
    }
}
```
 
Then create admin user

```
python manage.py createsuperuser
```
specify admin name, password and other details

Perform migrations by:

```
python manage.py makemigrations
python manage.py migrate
```
This will create migration scripts and update your local database with application models
## Usage

Start application
```
python manage.py runserver
```
This will run your app at http://127.0.0.1:8000/ 

To access admin console type in browser http://127.0.0.1:8000/admin

## Contributing
Please feel free to copy code, change it and use it as you wish :)
I was creating my project basing on bradtraversy's git project which can be found here https://github.com/bradtraversy/btre_project

## License
[MIT](https://choosealicense.com/licenses/mit/)