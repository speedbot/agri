from random import randint

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from agri.common.constants import THIRD_PARTY_API_URL
from agri.common.proxy import APIProxy


# A Simple DRF api to mock a system which has intermittent failure / issues
# The API intermittently produces a 400 / 500 error
class ThirdPartyApiViewSet(viewsets.GenericViewSet):
    queryset = ''

    def list(self, request, *args, **kwargs):
        random_number = randint(0, 5)
        if random_number == 0:
            return Response(status=HTTP_400_BAD_REQUEST)
        elif random_number == 1:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(
                data=APIProxy().get(THIRD_PARTY_API_URL), status=HTTP_200_OK,
            )
