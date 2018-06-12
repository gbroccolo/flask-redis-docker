import redis
from rq import Queue, Connection
from flask import Flask, request, jsonify

from long_task_package.long_task import long_task

app = Flask(__name__)
REDIS_URL = 'redis://redis:6379/0'
REDIS_QUEUES = ['default']


@app.route('/long_task', methods=['POST'])
def run_long_task():
    task_duration = int(request.form['duration'])
    with Connection(redis.from_url(REDIS_URL)):
        q = Queue()
        task = q.enqueue(long_task, task_duration)
    response_object = {
        'status': 'success',
        'data': {
            'task_id': task.get_id()
        }
    }
    return jsonify(response_object), 202


@app.route('/tasks/<task_id>', methods=['GET'])
def get_status(task_id):
    with Connection(redis.from_url(REDIS_URL)):
        q = Queue()
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            'status': 'success',
            'data': {
                'task_id': task.get_id(),
                'task_status': task.get_status(),
                'task_result': task.result,
            }
        }
    else:
        response_object = {'status': 'error'}
    return jsonify(response_object)


if __name__ == '__main__':
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=True, port=80)
    pass
