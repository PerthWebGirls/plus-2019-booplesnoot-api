from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .forms import RegistrationForm


from .serializers import UserSerializer, GroupSerializer, ProfileSerializer
from .models import Profile


def IndexView(request):
    url = "https://api.spoonacular.com/recipes/search?apiKey=3dc537f85d054e38a4caadd57f887609&number=5"

    r = requests.get(url.format()).json()
    # r is short for response

    recipe_list = {
        "title": r["results"][4]["title"],
        "image": r["results"][4]["image"],
        "servings": r["results"][4]["servings"],
        "time": r["results"][4]["readyInMinutes"],
    }

    context = {"recipe_list": recipe_list}

    return render(request, "recipefinderApp/recipefinder.html", context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello, World!"}
        return Response(content)

""""
Account view to show details for current logged in user
"""""

class AccountView(APIView):

    def get(self, request):
        if request.user is None:
            return Response({'error': 'Invalid Token'}, status=401)
        content = UserSerializer(request.user, context={'request': request}).data
        return Response(content)


"""
Registration view

"""
class RegistrationView(APIView):

    def post(self, request):
        form = RegistrationForm(request.data)

        if form.is_valid():
            user = form.save()
            content = UserSerializer(user, context={'request': request}).data
            return Response(content)
        else:
            return Response({ 'errors': form.errors }, status=422)




