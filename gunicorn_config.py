import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

bind = '0.0.0.0:8001'
worker_class = 'sync'
timeout = 30
loglevel = 'info'

#infolog = '/var/gunicorn-logs/info.log'
#errorlog = '/var/gunicorn-logs/error.log'