import requests


class APIProxy(object):
    DEFAULT_TIMEOUT = 30

    def __init__(self, headers=None):
        self.headers = headers

    def proxy(self, method, url, data=None):
        return self.make_request(
            method, url, headers=self.get_headers(), data=data or {}
        )

    def make_request(self, method, path, headers, data):
        return requests.request(
            method=method, url=path, timeout=self.DEFAULT_TIMEOUT, headers=headers,
            json=data
        )

    @staticmethod
    def generate_url(path, query_params=None):
        return '{}?{}'.format(path, query_params)

    def get_headers(self):
        default_headers = {
            'Content-Type': 'application/json',
        }

        if self.headers:
            default_headers.update(self.headers)

        return default_headers

    def get(self, path, query_params=None):
        return self.proxy('GET', self.generate_url(path, query_params))

    def create(self, path, query_params=None, data=None):
        return self.proxy('POST', self.generate_url(path, query_params), data=data)

    def update(self, data, path):
        return self.proxy('PATCH', self.generate_url(path), data=data)

    def delete(self, path, query_params=None):
        return self.proxy('DELETE', self.generate_url(path, query_params))
