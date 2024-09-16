import os
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def test():
    logger.info("Success! By Django :-)")
    return "Ok By Django"