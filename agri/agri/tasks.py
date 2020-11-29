import requests

from agri.common.tasks import Task


# A simple API which checks an api for a valid response and raises
# A request error on failure
# Basically a stub to call an intermittent API
class PollApi(Task):

    def _run(self, attempt=0, *args, **kwargs):
        url = 'http://127.0.0.1:8000/api/v1/third_party/'
        response = requests.get(url)
        response.raise_for_status()
        return '{} {}'.format(response.status_code, response.content[:20])
