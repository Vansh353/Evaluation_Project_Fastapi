from typing import Any, Optional
from fastapi import HTTPException, status
from dtos.base_response_model import BaseResponseModel, BaseErrorModel

# Importing libraries


class APIHelper:
    # Send error response with custom message
    def send_error_response(errorMessageKey: Optional[str] = None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=errorMessageKey or 'FAILURE')
    # Send unauthorized response with custom message
    def send_unauthorized_error(errorMessageKey: Optional[str] = None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=(BaseErrorModel(error=errorMessageKey or 'FAILURE')))
    
    # Send success response with custom message
    def send_success_response(data: Optional[Any] = None, successMessageKey: Optional[str] = None):
        return BaseResponseModel(data=data, message=successMessageKey or 'SUCCESS')
