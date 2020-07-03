from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from djoser.views import UserViewSet
from djoser import signals
from djoser.conf import settings
from djoser.compat import get_user_email

from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser


class CheckAvailabilityView(APIView):
    permission_classes = (AllowAny, )

    @staticmethod
    def get(request):
        username = request.query_params.get('username', None)
        email = request.query_params.get('email', None)

        if username is not None:
            if CustomUser.objects.filter(username=username).exists():
                return Response('That username is not available.', status=400)

        if email is not None:
            if CustomUser.objects.filter(email=email).exists():
                return Response(
                    'An account already exists with that email address.',
                    status=400
                )

        return Response(status=204)


class ExtendedUserViewSet(UserViewSet):
    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_active = True
        user.save()

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        if settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.confirmation(self.request, context).send(to)

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
