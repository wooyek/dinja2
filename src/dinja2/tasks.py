# coding=utf-8
import logging

from celery import shared_task
from celery.schedules import crontab
from celery.task import PeriodicTask
from django.utils import timezone

from . import models


@shared_task
def example_task(self):
    assert models
    logging.debug("timezone: %s", timezone.now())


# noinspection PyAbstractClass
class GitHubJobsSync(PeriodicTask):
    ignore_result = True
    run_every = crontab(hour=8, minute=0)
