flask-redis-docker
==================

An example about how to deploy a Flask application inside a Docker able to perform
asynchronous requests.

How it works
------------

Though Python allows asynchronous executions through several techniques, forking
asynchronous process from a main process in Docker is not trivial (see 
https://docs.docker.com/config/containers/multi-service_container/). The only
way is to define a `worker` process within the main processes of the container
(i.e. handled through `supervisor`, used as main process defined in the container's
`CMD`), that is able to perform operations in background.

Here, `Python Redis Queue` is used to define an asynchronous queue of required tasks
based on a `Redis` service, running on a separated (light) container.

How to run it
-------------

Once you have `docker-compose` installed, just create the images and the containers
through the command:

```
$ docker-compose up -d

```

This will create the two containers, the one with the Flask application listening
port `5000`, and the one with the `Redis` service (listening port `6379`).

```
$ docker-compose ps
 Name               Command               State               Ports            
-------------------------------------------------------------------------------
redis    docker-entrypoint.sh redis ...   Up      6379/tcp                     
webapp   /entrypoint.sh /start.sh         Up      443/tcp, 0.0.0.0:5000->80/tcp
```

Once both services are up and running in your localhost, you can submit a long running
request asynchronously as follows:

```
$ curl -X POST -F "duration=20" http://127.0.0.1:5000/long_task
{
  "data": {
    "task_id": "05aabf85-b34a-4797-8d44-8ad767a3928e"
  }, 
  "status": "success"
}
```

And retrieve the result with the following one:

```
$ curl -X GET http://127.0.0.1:5000/tasks/05aabf85-b34a-4797-8d44-8ad767a3928e
```

If the task is not concluded in the meantime, this is the response of the request:

```
{
  "data": {
    "task_id": "05aabf85-b34a-4797-8d44-8ad767a3928e", 
    "task_result": null, 
    "task_status": "started"
  }, 
  "status": "success"
}
```

Otherwise, this is the response with the output stored in the `task_result` key:

```
$ curl -X GET http://127.0.0.1:5000/tasks/05aabf85-b34a-4797-8d44-8ad767a3928e
{
  "data": {
    "task_id": "05aabf85-b34a-4797-8d44-8ad767a3928e", 
    "task_result": {
      "task": true
    }, 
    "task_status": "finished"
  }, 
  "status": "success"
}
```
