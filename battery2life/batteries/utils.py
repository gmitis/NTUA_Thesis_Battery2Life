import logging

logger = logging.getLogger('utils')

def log_request_response(request, response):        
    logger.info(f"Request Method: {request.method} | Request Resource: {request.get_full_path()}")     
    logger.info(f"Response Status: {response.status_code}")
