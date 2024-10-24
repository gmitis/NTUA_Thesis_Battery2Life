from rest_framework import viewsets
from .utils import log_request_response

class LoggingMixin(viewsets.ViewSet):
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        log_request_response(request, response)
        return response
