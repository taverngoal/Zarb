from old.app.modules.pybcs import httpc, common

try:
    from bae.api import logging
except:
    import logging
    from old.app.modules.pybcs.httpc import logger
    def init_logging(set_level = logging.INFO, 
                 console = True,
                 log_file_path = None):
        common.init_logging(httpc.logger, set_level, console, log_file_path)
    
from old.app.modules.pybcs.bcs import BCS
from old.app.modules.pybcs.bucket import Bucket

#modules should import
__all__ = ['bcs', 'bucket', 'object']


from old.app.modules.pybcs.common import NotImplementException
from old.app.modules.pybcs.common import md5_for_file

from old.app.modules.pybcs.httpc import *


#init_logging(logging.INFO, True, log_file_path='log/bcs.log')


