# Importing libraries
from typing import Any, Optional
from fastapi import HTTPException, status
from dtos.base_response_model import BaseResponseModel, BaseErrorModel

class APIHelper:
    # Send error response with custom message
  

    @staticmethod
    def send_error_response(errorMessage: Optional[str] = None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=errorMessage or 'Failure'
        )
    # Send unauthorized response with custom message
    @staticmethod
    def send_unauthorized_error(errorMessage: Optional[str] = None):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=BaseErrorModel(error=errorMessage or 'Unauthorized')
        )

    @staticmethod
    def send_success_response(successMessage: Optional[str] = None, data: Optional[dict] = None):
        return BaseResponseModel(data=data or "", message=successMessage or 'Success')