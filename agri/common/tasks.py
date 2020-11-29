from random import uniform

from billiard.exceptions import SoftTimeLimitExceeded
from celery.task import Task as CeleryTask
from django.db import DatabaseError, OperationalError
from requests import RequestException

from .utils import get_task_logger

task_logger = get_task_logger()


# A Base Celery task wrapper class which can be used to handle interaction
# with systems which have periodic failures
# If the task raises any errors we retry the task with exponential backoff till it succeeds
# we can modify the minimum_delay_time / max retries based on the use cases
class Task(CeleryTask):
    default_retry_delay = 30
    max_retries = 5
    retry_on_time_limit_exceeded = False
    minimum_delay_time = 10

    def run(self, *args, **kwargs):
        try:
            return self._run(*args, **kwargs)
        except (OperationalError, DatabaseError, RequestException) as exc:
            raise self.retry(
                exc=exc,
                countdown=self.minimum_delay_time + int(uniform(2, 4) ** self.request.retries)
            )
        except SoftTimeLimitExceeded as exc:
            if self.retry_on_time_limit_exceeded:
                raise self.retry(exc=exc)
        get_task_logger().error(
            'Task failure {}: {}'.format(exc.__class__.__name__, exc),
            exc_info=True,
            extra={'run_args': args, 'run_kwargs': kwargs},
        )

    def _run(self, *args, **kwargs):
        raise NotImplementedError('Must define _run method.')
