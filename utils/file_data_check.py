from player.models import Player,Country,Match
from rest_framework.response import Response

def PlayerInDatabaseValidCheck(country_id):
    player_qs=Player.objects.filter(country_id=country_id, is_deleted=False)
    if not player_qs:
        return Response({"mag":"Player does not exist"})
    return player_qs
    
def MatchInDatabaseValidCheck(match_id):
    match_qs=Match.objects.filter(country_id=match_id, is_deleted=False)
    if not match_qs:
        return Response({"mag":"Match does not exist"})
    return match_qs

def CountryInDatabaseValidCheck(country_id):
    country_qs=Country.objects.filter(id=country_id, is_deleted=False)
    if not country_qs:
        return Response({"mag":"Country does not exist"})
    return country_qs