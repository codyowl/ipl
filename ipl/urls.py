"""ipl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import TopFourTeamWins, TossesWon, MaxPlayerOfMatch, \
MaxMatchesTeam, MaxWinLocation, PerBatDecision, MaxWinLosePerLocation, MaxWinTeamRuns, \
MaxWinTeamWickets, TeamWonTossAndMatch


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('top-four-teams/', TopFourTeamWins.as_view()),
	path('most-tosses-won/', TossesWon.as_view()),
	path('max-player-of-match/', MaxPlayerOfMatch.as_view()),
	path('max-matches-team/', MaxMatchesTeam.as_view()),
	path('max-win-location/', MaxWinLocation.as_view()),
	path('per-bat-decision/', PerBatDecision.as_view()),
	path('max-winlose-per-location/', MaxWinLosePerLocation.as_view()),
	path('max-win-team-runs/', MaxWinTeamRuns.as_view()),
	path('max-win-team-wickets/', MaxWinTeamWickets.as_view()),
	path('team-won-match-toss/', TeamWonTossAndMatch.as_view()),

]
