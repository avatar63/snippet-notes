# gunicorn.conf.py

import multiprocessing

bind = "0.0.0.0:8000"  # Bind to the appropriate address and port
workers = multiprocessing.cpu_count() * 2 + 1  # Use multiple workers for better performance
#errorlog = '/var/log/gunicorn/error.log'  # Specify error log file path
#accesslog = '/var/log/gunicorn/access.log'  # Specify access log file path
