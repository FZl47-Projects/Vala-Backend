from rest_framework.exceptions import APIException
from rest_framework import status


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    
class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN