proc_name = 'waterbear'
bind = '127.0.0.1:8000'
workers = 3
user = 'root'
group = 'www-data'
loglevel = 'debug'
errorlog = '/home/ubuntu/gunicorn.error.log'
accesslog = '/home/ubuntu/gunicorn.access.log'
