from rest_framework_jwt import views as jwt_views

from . import serializers
from .throttling import AuthTokenThrottler, CodeTokenThrottler


class ObtainCodeToken(jwt_views.ObtainJSONWebTokenView):
    serializer_class = serializers.CodeTokenSerializer
    throttle_classes = [CodeTokenThrottler]


class ObtainAuthToken(jwt_views.ObtainJSONWebTokenView):
    serializer_class = serializers.AuthTokenSerializer
    throttle_classes = [AuthTokenThrottler]


class RefreshAuthToken(jwt_views.RefreshJSONWebTokenView):
    pass


class VerifyAuthToken(jwt_views.VerifyJSONWebTokenView):
    pass


obtain_code_token = ObtainCodeToken.as_view()
obtain_auth_token = ObtainAuthToken.as_view()
refresh_auth_token = RefreshAuthToken.as_view()
verify_auth_token = VerifyAuthToken.as_view()
