import requests
from generate_token import Generate_token


def get_albums(id):
    token=Generate_token.authorization()
    header={'Authorization':token}
    response=requests.get(f'https://api.spotify.com/v1/albums/{id}')
    return response