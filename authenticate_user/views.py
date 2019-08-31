from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model
from .forms import SignUp
from .serializers import SignupSerializer

User = get_user_model()

class SignUpViewSet(ViewSet):

    def list(self, request):
        return render(request, 'authenticate_user_templates/signup.html', {'signup': SignUp})

    def create(self, request):
        user = User()
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.username = serializer.validated_data['username']
        user.email = serializer.validated_data['email']
        user.staff_member = serializer.validated_data['staff_member']
        user.password = serializer.validated_data['password']
        user.save()
        return HttpResponse("Your SIgnup data is saved")