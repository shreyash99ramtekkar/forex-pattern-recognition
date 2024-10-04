from constants import LoggerConstants
import logging,logging.config;

class FxPatternRecognitionLogger:
    def __init__(self):
        logging.config.fileConfig(LoggerConstants.CONFIG_PATH,disable_existing_loggers=False)
    
    def get_logger(self,name):
        return logging.getLogger(name)