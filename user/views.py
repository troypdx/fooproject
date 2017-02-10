from django.shortcuts import render
<<<<<<< HEAD
=======

# Create your views here.
>>>>>>> 63bc29be35200884c5b1197117877b1229d58d5b
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
<<<<<<< HEAD
# Expose Django's User object...
=======
>>>>>>> 63bc29be35200884c5b1197117877b1229d58d5b
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
<<<<<<< HEAD
=======

>>>>>>> 63bc29be35200884c5b1197117877b1229d58d5b
