from flask import Flask, send_from_directory
from flask_cors import CORS
import multiprocessing
import consumer

consumer = consumer.Consumer()

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/api/memory')
def memory():
    value = consumer.get_memory_metrics()
    return {'value': value}

@app.route('/api/cpu')
def cpu():
    value = consumer.get_cpu_metrics()
    return {'value': value}

@app.route('/api/total_core')
def core_count():
    num_cores = multiprocessing.cpu_count()
    return {'value': num_cores}

@app.route('/api/core')
def core():
    value = consumer.get_cpu_core_metrics()
    return value

@app.route('/api/processes')
def process():
    value = consumer.get_process_metrics()
    return value

@app.route('/api/network')
def network():
    value = consumer.get_network_metrics()
    return value

@app.route('/', defaults={'p': "index.html"})
@app.route('/<path:p>')
def index(p):
    return send_from_directory('web', p)

if __name__ == '__main__':
    app.run()
