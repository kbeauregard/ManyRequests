import requests
from threading import Thread
from six.moves.queue import Queue


def flatten_kwargs(index, **kwargs):
    kwargs = dict(kwargs)
    for arg in kwargs:
        if isinstance(kwargs[arg], list):
            kwargs[arg] = kwargs[arg][index]
    return kwargs


class WebRunner:
    resp_queue = None


    def __init__(self):
        self.resp_queue = Queue()


    def request(self, index, url, **kwargs):
        kwargs = flatten_kwargs(index, **kwargs)
        try:
            method = kwargs.pop('method', 'GET')
            self.resp_queue.put(
                (index, requests.request(method=method, url=url, **kwargs))
            )
        except Exception as e:
            self.resp_queue.put((index, None))
            print('Failed to download %s because %s.' % (url, e))


    def runner(self, **kwargs):
        while True:
            index, url = self.work_queue.get()
            if 'http://' not in url and 'https://' not in url:
                url = 'http://' + url
            self.request(index, url, **kwargs)
            self.work_queue.task_done()


    def run(self, urls, concurrency=4, **kwargs):
        self.work_queue = Queue()
        for url in enumerate(urls):
            self.work_queue.put(url)
        for i in range(concurrency):
            t = Thread(target=self.runner, kwargs=kwargs)
            t.daemon = True
            t.start()
        self.work_queue.join()
        responses = list(self.resp_queue.queue)
        responses = sorted(responses, key=lambda x: x[0])
        return [r[1] for r in responses]
