import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        fh = logging.FileHandler("logger.log")
        fh.setLevel(logging.DEBUG) 
        #formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)       
        #Add handlers
        logger.addHandler(fh)   
    return logger    