from rest_framework.response import Response


def success_response(data=None, message="Success"):

    return Response({
        "success": True,
        "message": message,
        "data": data
    })