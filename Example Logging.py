__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import logging
import logging.config

logging.config.fileConfig("configuration.cfg")

log = logging.getLogger("BetaSeries")
log.debug("unspec - debug")
log.error("unspec - error")