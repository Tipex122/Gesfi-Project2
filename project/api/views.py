from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from project.users.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer, GroupSerializer


def index(request):
    users = User.objects.all()
    nbr = users.count()
    context = {'users': users, 'nbr': nbr, }
    return render(request, 'pages/home.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

