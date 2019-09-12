import logging

LOG = logging.getLogger()


def lambda_handler(_event: dict, _context):
    LOG.debug('Initialising')
    LOG.info('Processing')
    LOG.warn('Success')
    LOG.error('Failure')
    LOG.critical('Bananas')
