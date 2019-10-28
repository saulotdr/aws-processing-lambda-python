from locust import HttpLocust, TaskSet, task

file = open('../../res/bigdoc.json')
doc = file.read()

class UploaderTasks(TaskSet):
    @task
    def sendEventLogs(self):
        self.client.post('/logs', doc, headers={'content-type': 'application/json'}, cert=('../../res/cert.pem', '../../res/cert.key'))

class Uploader(HttpLocust):
    min_wait = 1000
    max_wait = 1000
    task_set = UploaderTasks
    host = '?' # todo: insert correct url here
