import logging
from .ML.kernel_smoother import kernel_smoother
from .ML.SVR import SVR_rbf

logger = logging.getLogger(__name__)

operation_dict = {
    'Kernel Smoother': kernel_smoother,
    'SVR': SVR_rbf
}


def handle_job(job):
    logger.info('Handling job {}'.format(job))
    try:
        func = operation_dict.get(job['name'], None)
        op_args = job.get('params', [])
        kwargs = {}
        for pair in op_args:
            kwargs[pair['name']] = pair['value']
        result = func(**kwargs)
    except Exception as e:
        logger.exception("ERROR: %s" % (e))
        return None

    return result
