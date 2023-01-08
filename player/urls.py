from django.urls import path
from player.views import AddCountry, UpdateCountry, GetCountry, AddPlayer, UpdatePlayer, GetPlayer

urlpatterns = [
    path('country', AddCountry.as_view()),
    path('team/country/<int:country_id>/players', AddPlayer.as_view()),
    path('team/country/update/<int:country_id>', UpdateCountry.as_view()),
    path('team/country/<int:country_id>', GetCountry.as_view()),
    path('team/country/<int:country_id>/players/<int:player_id>', UpdatePlayer.as_view()),
    path('team/country/<int:country_id>/player/<int:player_id>', GetPlayer.as_view()),
    # path('team/country/<int:country_id>/players/<int:player_id>', GetCountry.as_view()),
    # path('team/country/<int:country_id>/players/<int:player_id>', GetCountry.as_view()),
]




"""
base_url = https://127.0.0.1:8000/v1/fixture/

1. Teams
    1. Countries
        POST  --  Add country to table {name(char), flag(media), continent(char)}
        GET  --  Getch all countries in database which are active
                -> display total number of players in the team
        PUT  --  Update info about a country - team/country/<int:country_id>
        DELETE  --  Delete a country - team/country/<int:country_id>
        
        GET  --  Fetch info about a single country - team/country/<int:country_id>
        
    2. Players
        POST  --  Add player to table - team/country/<int:country_id>/players
        GET  --  get player from table - team/country/<int:country_id>/players
        PUT  --  Update info about a player - team/country/<int:country_id>/players/<int:player_id>
        DELETE  --  Delete a player - team/country/<int:country_id>/players/<int:player_id>
        
        GET  --  Fetch info of a single player - team/country/<int:country_id>/players/<int:player_id>
        
    3. Matches
    
        1.matches
            POST  --  Schedule a match between two team - match/
            GET  --  get all matches from table - match/ (pagination,p=1$psz=20)
                    -> Additional filter :- &team=1
                    -> Venue :- &venue=qatar
                    -> datetimefield :- &op=lt&date=2023-01-01
            PUT  --  Update match data - match/<int:match_id>
            DELETE  --  Delete a match - match/<int:match_id>
            
            GET  --  Fetch info of a single match - match/<int:match_id>
        
        2. match_teams (Not required)
            POST  --  Add team entry - match/

        3. match_players
            POST  --  Add players to matches - match/<int:match_id>/team/<int:match_teams_id>/player
                -> limit entry to 20 players
  
        
"""