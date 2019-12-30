# ipl
Webservice built with DRF to get insights for IPL Matches with some datas

## api routes:
 - http://127.0.0.1:8000/top-four-teams/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/most-tosses-won/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-player-of-match/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-matches-team/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-win-location/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/per-bat-decision/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-winlose-per-location/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-win-team-runs/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/max-win-team-wickets/?year=<SEASON_YEAR>
 - http://127.0.0.1:8000/team-won-match-toss/?year=<SEASON_YEAR>&team_name=<TEAM_NAME>

## prerequisites installation:
    pip3 install -r requirements.txt
    
## steps before running the webservice:
    create a database on mysql with the name "ipl"  
    
## Management commands to migrate the models to db
    python manage.py makemigrations
    python manage.py migrate
    
## Management commands to dump data to db from csv:
    python manage.py migrate_match_to_db
    python manage.py migrate_delivery_to_db
    
## To run the server on local machine:
    python manage.py runserver 
    
## Endpoints sample on postman:

### to get top 4 teams in terms of win
![1top4](https://user-images.githubusercontent.com/9798362/71595952-a6e4f180-2b63-11ea-89e5-b6997f36a25f.png)
### to get team that won most number of tosses
![2tosswon](https://user-images.githubusercontent.com/9798362/71595954-a9dfe200-2b63-11ea-9015-b63f4308ff47.png)
### to get player that won maximum player of the match
![3](https://user-images.githubusercontent.com/9798362/71595957-aba9a580-2b63-11ea-86b4-22f8d32128a0.png)
### to get team that won max matches
![4](https://user-images.githubusercontent.com/9798362/71595958-ad736900-2b63-11ea-923f-ffcad456b0d1.png)
### to get location that has most number of wins
![5](https://user-images.githubusercontent.com/9798362/71595961-af3d2c80-2b63-11ea-9aa6-aeef2074bd64.png)
### to get percentage of bat decision
![6](https://user-images.githubusercontent.com/9798362/71595963-b19f8680-2b63-11ea-8e40-2145523cd277.png)
### to get location hosted most number of matches and win and loss %
![7](https://user-images.githubusercontent.com/9798362/71595964-b3694a00-2b63-11ea-8c2f-55acd4a2ee8d.png)
### to get the team with highest margin for runs for the season
![8](https://user-images.githubusercontent.com/9798362/71595965-b49a7700-2b63-11ea-9712-35154897235a.png)
### to get team that win by highest number of wicket
![9](https://user-images.githubusercontent.com/9798362/71595967-b6643a80-2b63-11ea-9c74-14ffc28446ad.png)
### to get how many times a team won match and toss
![10](https://user-images.githubusercontent.com/9798362/71595970-b8c69480-2b63-11ea-9ed4-c5ceafded3b7.png)
