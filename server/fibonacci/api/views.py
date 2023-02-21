from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from fibonacci.tasks import fibonacci_task


class GetFibonnaciAPIView(APIView):
    def get(self, request: Request,number):
        print('lol')
        fibonacci_task.delay({'number': number})
        return Response("done")
