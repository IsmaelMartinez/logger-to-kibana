import logging
from datetime import datetime

LOG = logging.getLogger()


def lambda_handler(event, context):
    LOG.info('lambda_handler called')
    return {'message': datetime.now()}
