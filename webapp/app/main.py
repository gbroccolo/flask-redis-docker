import redis
from rq import Connection
from flask import Flask, request, jsonify

from long_task_package import long_task

app = Flask(__name__)
REDIS_URL = 'redis://redis:6379/0'
REDIS_QUEUES = ['default']

@app.route('/long_task', methods=['POST'])
def run_long_task():
    with Connection(redis.from_url(REDIS_URL)):
        q = Queue()
        task = q.enqueue(create_task, task_type)
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
    app.run(host='0.0.0.0', debug=True, port=5000)
