from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response



def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == status.HTTP_403_FORBIDDEN:
            response.data['message'] = "You are not allowed to access."
        elif response.status_code == status.HTTP_204_NO_CONTENT:
            response.data['message'] = "No content for this request."
        return response

    return Response(
        {"results": {}, "message": "An unexpected error occurred.", "status": "failed"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )