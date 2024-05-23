import logging

def before_all(context):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Before all test...')
    context.logger = logger