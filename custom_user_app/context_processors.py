from django.conf import settings


def auth_user_model(request):
    display = settings.AUTH_USER_MODEL
    return {"display": display}
