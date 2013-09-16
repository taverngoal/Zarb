from app.modules.pybcs import httpc, common

try:
    from bae.api import logging
except:
    import logging
    from app.modules.pybcs.httpc import logger
    def init_logging(set_level = logging.INFO, 
                 console = True,
                 log_file_path = None):
        common.init_logging(httpc.logger, set_level, console, log_file_path)
    
from app.modules.pybcs.bcs import BCS
from app.modules.pybcs.bucket import Bucket

#modules should import
__all__ = ['bcs', 'bucket', 'object']


from app.modules.pybcs.common import NotImplementException
from app.modules.pybcs.common import md5_for_file

from app.modules.pybcs.httpc import *


#init_logging(logging.INFO, True, log_file_path='log/bcs.log')


