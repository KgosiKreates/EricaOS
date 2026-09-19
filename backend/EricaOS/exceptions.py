from rest_framework.views import exception_handler

def erica_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return response

    # reshape response here
    outgoing = {
        success: exc.detail
    }

    return response