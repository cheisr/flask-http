# flask_web/app.py

from flask import Flask
from prometheus_client import start_http_server, Counter, Summary

app = Flask(__name__)

call_metric = Counter('opsschool_monitor_flask_main_count', 'Number of visits to main', [ "service", "endpoint" ])
time_metric = Summary('opsschool_monitor_flask_request_processing_seconds', 'Time spent processing request', [ "method" ])


hello_world_timer = time_metric.labels(method="hello_world")
@app.route('/')
@hello_world_timer.time()
def hello_world():
    call_metric.labels(service='opsschool_flask', endpoint='main').inc(1)
    return 'Hey, we have Flask in a Docker container!'


goaway_timer = time_metric.labels(method="goaway")
@app.route('/goaway')
@goaway_timer.time()
def goaway():
    call_metric.labels(service='opsschool_flask', endpoint='goaway').inc(1)
    return 'GO AWAY!'


if __name__ == '__main__':
    start_http_server(5001)
    app.run(debug=False, host='0.0.0.0')
