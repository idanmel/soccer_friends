"""soccer_friends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
from tournaments import views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'tournaments', views.TournamentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url('^tournaments/(?P<pk>[0-9]+)/matches/$', views.MatchesList.as_view()),
    url('^tournaments/(?P<pk>[0-9]+)/stages/$', views.StagesList.as_view()),
    url('^match-predictions/$', views.match_predictions),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
