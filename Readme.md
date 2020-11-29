### Clone The Repo

`git clone git@github.com:speedbot/.git`

### Set up the virtual environment

`virtualenv -p python3 venv`

### Activate the virtual environment and install deps
`source venv/bin/activate`
``pip install -r reqs``

### Run migrations

`python manage.py migrate`

### Run the Dev server 

`python manage.py runserver`

### Url list

- Mock Third party api with intermittent response `http://127.0.0.1:8000/api/v1/third_party/`

### Start Celery 

`celery -A agri  worker --loglevel=info
`

` celery -A agri flower`