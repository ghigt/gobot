__author__ = 'Alexandre Cloquet'

import logging
import logging.config

logging.config.fileConfig("configuration.cfg")

log = logging.getLogger("BetaSeries")
log.debug("unspec - debug")
log.error("unspec - error")